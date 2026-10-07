import importlib.util
from pathlib import Path
import tempfile
import unittest

PATH = Path(__file__).resolve().parents[1]/'skills/repo-onboarding-map/scripts/inventory.py'
spec = importlib.util.spec_from_file_location('inventory', PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class InventoryTests(unittest.TestCase):
    def test_markers_depth_and_exclusions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'README.md').write_text('synthetic')
            (root/'.env').write_text('never read')
            (root/'src/deep').mkdir(parents=True)
            (root/'src/deep/package.json').write_text('{}')
            (root/'node_modules').mkdir()
            (root/'node_modules/package.json').write_text('{}')
            result = module.inventory(root, depth=0)
            self.assertEqual(result['markers'], ['README.md'])
            self.assertEqual(result['directories'], ['src'])
            result = module.inventory(root, depth=2)
            self.assertEqual(result['markers'], ['README.md','src/deep/package.json'])
    def test_budget_and_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for n in range(5):
                (root/str(n)).mkdir()
            self.assertTrue(module.inventory(root, max_entries=2)['truncated'])
            with self.assertRaises(ValueError):
                module.inventory(root, depth=-1)
    def test_link_does_not_escape(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            (Path(outside)/'package.json').write_text('{}')
            try:
                (root/'linked').symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest('OS does not permit symlink creation')
            result = module.inventory(root)
            self.assertEqual(result['markers'], [])
            self.assertTrue(result['warnings'])
