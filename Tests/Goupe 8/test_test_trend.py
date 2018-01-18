# -*- coding: utf-8 -*-

from fonction_G8 import test_trend


def test_test_trend():
     
      data_pas_de_tend = {'avalanche': [[1, 2, 2], [3, 4, 2]]}
      assert str(test_trend(data_pas_de_tend,"avalanche",1)) == "('avalanche', 'Pas_de_tendance')"