

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement
from ._AttrMixinPoints import _AttrMixinPoints
from ._AttrMixinStyle import _AttrMixinStyle




class SVGPolygon(AbstractSVGElement, _AttrMixinPoints, _AttrMixinStyle):

	def __init__(self):
		super().__init__("polygon")
	#

	def getBoundingPoints(self):
		yield from super().getBoundingPoints()
		for cx, cy in self._points:
			yield cx, cy
	#

#












