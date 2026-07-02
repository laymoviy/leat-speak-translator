class Colors:
    PRIMARY = "#1e88e5"
    PRIMARY_HOVER = "#1976d2"
    PRIMARY_DARK = "#1565c0"
    
    SECONDARY = "#26a69a"
    SECONDARY_HOVER = "#00897b"
    
    SUCCESS = "#66bb6a"
    WARNING = "#ffa726"
    DANGER = "#ef5350"
    
    BACKGROUND = "#0d1117"
    BACKGROUND_SECONDARY = "#161b22"
    BACKGROUND_TERTIARY = "#1c2128"
    
    SURFACE = "#21262d"
    SURFACE_HOVER = "#30363d"
    
    TEXT_PRIMARY = "#e6edf3"
    TEXT_SECONDARY = "#8b949e"
    TEXT_DISABLED = "#6e7681"
    
    ACCENT = "#ff6b6b"
    ACCENT_HOVER = "#ff5252"
    
    BORDER = "#30363d"
    BORDER_HOVER = "#484f58"
    
    INPUT_BG = "#0d1117"
    INPUT_BORDER = "#30363d"
    INPUT_BORDER_FOCUS = "#1e88e5"


class Fonts:
    FAMILY = "Segoe UI"
    FAMILY_MONO = "Consolas"
    
    SIZE_SMALL = 11
    SIZE_NORMAL = 13
    SIZE_MEDIUM = 14
    SIZE_LARGE = 16
    SIZE_XLARGE = 20
    SIZE_TITLE = 28


class Spacing:
    XS = 4
    SM = 8
    MD = 12
    LG = 16
    XL = 20
    XXL = 24
    XXXL = 32


class BorderRadius:
    SMALL = 6
    MEDIUM = 8
    LARGE = 12
    XLARGE = 16


class Shadows:
    SMALL = "0 2px 4px rgba(0, 0, 0, 0.3)"
    MEDIUM = "0 4px 8px rgba(0, 0, 0, 0.4)"
    LARGE = "0 8px 16px rgba(0, 0, 0, 0.5)"


class ButtonStyles:
    PRIMARY = {
        "fg_color": Colors.PRIMARY,
        "hover_color": Colors.PRIMARY_HOVER,
        "text_color": Colors.TEXT_PRIMARY,
        "border_width": 0,
        "corner_radius": BorderRadius.MEDIUM
    }
    
    SECONDARY = {
        "fg_color": Colors.SECONDARY,
        "hover_color": Colors.SECONDARY_HOVER,
        "text_color": Colors.TEXT_PRIMARY,
        "border_width": 0,
        "corner_radius": BorderRadius.MEDIUM
    }
    
    DANGER = {
        "fg_color": Colors.DANGER,
        "hover_color": "#e53935",
        "text_color": Colors.TEXT_PRIMARY,
        "border_width": 0,
        "corner_radius": BorderRadius.MEDIUM
    }
    
    OUTLINE = {
        "fg_color": "transparent",
        "hover_color": Colors.SURFACE_HOVER,
        "text_color": Colors.PRIMARY,
        "border_width": 2,
        "border_color": Colors.PRIMARY,
        "corner_radius": BorderRadius.MEDIUM
    }
    
    GHOST = {
        "fg_color": "transparent",
        "hover_color": Colors.SURFACE,
        "text_color": Colors.TEXT_SECONDARY,
        "border_width": 0,
        "corner_radius": BorderRadius.MEDIUM
    }


class FrameStyles:
    PRIMARY = {
        "fg_color": Colors.SURFACE,
        "border_width": 1,
        "border_color": Colors.BORDER,
        "corner_radius": BorderRadius.LARGE
    }
    
    SECONDARY = {
        "fg_color": Colors.BACKGROUND_SECONDARY,
        "border_width": 0,
        "corner_radius": BorderRadius.MEDIUM
    }
    
    CARD = {
        "fg_color": Colors.SURFACE,
        "border_width": 1,
        "border_color": Colors.BORDER,
        "corner_radius": BorderRadius.XLARGE
    }


class TextboxStyles:
    DEFAULT = {
        "fg_color": Colors.INPUT_BG,
        "border_width": 2,
        "border_color": Colors.INPUT_BORDER,
        "corner_radius": BorderRadius.MEDIUM,
        "text_color": Colors.TEXT_PRIMARY
    }


class LabelStyles:
    TITLE = {
        "text_color": Colors.TEXT_PRIMARY,
        "font": (Fonts.FAMILY, Fonts.SIZE_TITLE, "bold")
    }
    
    HEADING = {
        "text_color": Colors.TEXT_PRIMARY,
        "font": (Fonts.FAMILY, Fonts.SIZE_LARGE, "bold")
    }
    
    BODY = {
        "text_color": Colors.TEXT_PRIMARY,
        "font": (Fonts.FAMILY, Fonts.SIZE_NORMAL)
    }
    
    SECONDARY = {
        "text_color": Colors.TEXT_SECONDARY,
        "font": (Fonts.FAMILY, Fonts.SIZE_NORMAL)
    }
    
    SMALL = {
        "text_color": Colors.TEXT_SECONDARY,
        "font": (Fonts.FAMILY, Fonts.SIZE_SMALL)
    }


class SegmentedButtonStyles:
    DEFAULT = {
        "fg_color": Colors.SURFACE,
        "selected_color": Colors.PRIMARY,
        "selected_hover_color": Colors.PRIMARY_HOVER,
        "unselected_color": Colors.SURFACE,
        "unselected_hover_color": Colors.SURFACE_HOVER,
        "text_color": Colors.TEXT_PRIMARY,
        "border_width": 1,
        "corner_radius": BorderRadius.MEDIUM
    }


class WindowStyles:
    MAIN = {
        "fg_color": Colors.BACKGROUND
    }
    
    DIALOG = {
        "fg_color": Colors.BACKGROUND_SECONDARY
    }


class AnimationDurations:
    FAST = 0.15
    NORMAL = 0.25
    SLOW = 0.35


class Transitions:
    EASE_IN_OUT = "ease-in-out"
    EASE_IN = "ease-in"
    EASE_OUT = "ease-out"
