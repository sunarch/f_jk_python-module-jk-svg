

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinMaskContentUnits:

	@property
	def maskContentUnits(self) -> str:
		return self._attributes.get("maskContentUnits", "userSpaceOnUse")
	#

	@maskContentUnits.setter
	def maskContentUnits(self, v:str):
		assert v in [ "userSpaceOnUse", "objectBoundingBox" ]
		self._attributes["maskContentUnits"] = v
	#

#











