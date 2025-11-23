import pathlib
import importlib.util
import unittest

import numpy as np
import numpy.testing as npt


def load_module():
    here = pathlib.Path(__file__).resolve().parent
    module_path = here.parent / "Numpy_Vectorization.py"
    spec = importlib.util.spec_from_file_location("numpy_vect", str(module_path))
    # Can't proceed without a valid spec and loader so raise an error to prevent mypy warnings
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot create module spec or loader for {module_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestSmallNumpyVectorization(unittest.TestCase):
    def test_lazy_report_computes_results(self):
        mod = load_module()
        np.random.seed(0)
        inst = mod.Small_Numpy_Vectorization()
        # After init, results should be uncomputed
        self.assertIsNone(inst.c_non_vectorized)
        self.assertIsNone(inst.c_vectorized)
        # Calling report should compute missing results lazily
        results = inst.report(quiet=True)
        # report() should return a tuple of (non_vectorized, vectorized)
        self.assertIsInstance(results, tuple)
        self.assertEqual(len(results), 2)
        c_non, c_vec = results
        self.assertIsNotNone(c_non)
        self.assertIsNotNone(c_vec)
        self.assertTrue(np.array_equal(c_non, c_vec))

    def test_methods_return_equal(self):
        mod = load_module()
        np.random.seed(1)
        inst = mod.Small_Numpy_Vectorization()
        c1 = inst.non_vectorized_addition(quiet=True)
        c2 = inst.vectorized_addition(quiet=True)
        npt.assert_array_equal(c1, c2)


if __name__ == "__main__":
    unittest.main()
