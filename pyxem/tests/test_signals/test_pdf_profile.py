# -*- coding: utf-8 -*-
# Copyright 2017-2019 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import numpy as np

from pyxem.signals.pdf_profile import PDFProfile


def test_generate_signal():
    data = np.ones((1, 10)) * np.arange(4).reshape(4, 1)
    data = data.reshape(2, 2, 10)
    pdf = PDFProfile(data)
    assert isinstance(pdf, PDFProfile)


def test_generate_signal():
    data = np.ones((1, 10)) * np.arange(4).reshape(4, 1)
    data = data.reshape(2, 2, 10)
    pdf = PDFProfile(data)
    pdf.normalise_signal()
    assert np.equal(pdf, np.ones((2, 2, 10)))