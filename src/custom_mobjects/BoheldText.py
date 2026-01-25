from manim import Text, ManimColor, register_font
from manim import constants as const
from typing import Self

class BoheldText(Text):
    def __init__(self, text: str, render_shadow=True, fill_opacity=1.0, stroke_width=0, *, color=ManimColor("#e4c8c8"), font_size=48, line_spacing=-1, slant='NORMAL', weight='NORMAL', t2c=None, t2f=None, t2g=None, t2s=None, t2w=None, gradient=None, tab_width=4, warn_missing_font=True, height=None, width=None, should_center=True, disable_ligatures=False, use_svg_cache=False, **kwargs):
        # Be sure to have the font installed on your PC!
        with register_font("src/assets/fonts/custom-BoheldFreeDEMO-Regular.otf"):
            super().__init__(text, fill_opacity, stroke_width, color, font_size, line_spacing, 'Boheld Free DEMO', slant, weight, t2c, t2f, t2g, t2s, t2w, gradient, tab_width, warn_missing_font, height, width, should_center, disable_ligatures, use_svg_cache, **kwargs)
            if (render_shadow):
                self.add(self.get_shadow())

    def get_shadow(self: Self, clr=ManimColor("#82001e")) -> Self:
        return self.copy()\
            .set_color(clr)\
            .shift(const.DL * .050)\
            .set_z_index(-1)