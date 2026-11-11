import pytest

from employee import Employee

@pytest.fixture
def karyawan():
    """Satu karyawan yang dipakai semua fungsi tes."""
    karyawan = Employee('Franka', 'Solo', 50000)
    return karyawan

def test_give_default_raise(karyawan):
    """Kenaikan default: gaji naik 5000."""
    karyawan.give_raise()
    assert karyawan.salary == 55000

def test_give_custom_raise(karyawan):
    """Kenaikan khusus: gaji naik sejumlah yang diminta."""
    karyawan.give_raise(10000)
    assert karyawan.salary == 60000
