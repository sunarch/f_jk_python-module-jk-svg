

import typing

import jk_typing
import jk_hwriter

from .AbstractSVGElement import AbstractSVGElement




class _AttrMixinR:

	@property
	def r(self) -> float:
		return self._attributes.get("r", 0)
	#

	@r.setter
	def r(self, v:float):
		self._attributes["r"] = v
	#

#












