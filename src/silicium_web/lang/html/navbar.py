from silicium import Component


class Nav(Component):
	"""Build Navbar Component"""
	build_target = "html"

	@property
	def code(self) -> str:
		return f"<nav></nav>"
