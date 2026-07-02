import customtkinter as ctk
from styles import (
    Colors, Fonts, Spacing, BorderRadius,
    ButtonStyles, FrameStyles, LabelStyles,
    SegmentedButtonStyles, WindowStyles
)

class SettingsWindow:
    def __init__(self, parent, settings, translations, on_language_change):
        self.parent = parent
        self.settings = settings
        self.translations = translations
        self.on_language_change = on_language_change
        self.window = None
    
    def open(self):
        if self.window is not None and self.window.winfo_exists():
            self.window.focus()
            return
        
        ui_lang = self.settings.get("ui_language")
        
        self.window = ctk.CTkToplevel(self.parent)
        self.window.title(self.translations.get("settings_title", ui_lang))
        self.window.geometry("500x320")
        self.window.resizable(False, False)
        self.window.transient(self.parent)
        self.window.grab_set()
        self.window.configure(**WindowStyles.DIALOG)
        
        center_x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - 250
        center_y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - 160
        self.window.geometry(f"+{center_x}+{center_y}")
        
        header_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        header_frame.pack(fill="x", padx=Spacing.XXL, pady=(Spacing.XXL, Spacing.LG))
        
        icon = ctk.CTkLabel(
            header_frame,
            text="⚙",
            font=(Fonts.FAMILY, 32),
            text_color=Colors.PRIMARY
        )
        icon.pack(side="left", padx=(0, Spacing.MD))
        
        title = ctk.CTkLabel(
            header_frame,
            text=self.translations.get("settings_title", ui_lang),
            font=(Fonts.FAMILY, Fonts.SIZE_XLARGE, "bold"),
            text_color=Colors.TEXT_PRIMARY
        )
        title.pack(side="left")
        
        main_frame = ctk.CTkFrame(self.window, **FrameStyles.CARD)
        main_frame.pack(fill="both", expand=True, padx=Spacing.XXL, pady=(0, Spacing.LG))
        
        content = ctk.CTkFrame(main_frame, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=Spacing.XL, pady=Spacing.XL)
        
        lang_icon = ctk.CTkLabel(
            content,
            text="🌍",
            font=(Fonts.FAMILY, 20)
        )
        lang_icon.pack(anchor="w", pady=(0, Spacing.SM))
        
        ui_lang_label = ctk.CTkLabel(
            content,
            text=self.translations.get("ui_language", ui_lang),
            font=(Fonts.FAMILY, Fonts.SIZE_MEDIUM, "bold"),
            text_color=Colors.TEXT_PRIMARY
        )
        ui_lang_label.pack(anchor="w", pady=(0, Spacing.MD))
        
        ui_lang_selector = ctk.CTkSegmentedButton(
            content,
            values=[
                self.translations.get("english", ui_lang),
                self.translations.get("russian", ui_lang)
            ],
            command=lambda val: self.change_ui_language(val),
            height=40,
            font=(Fonts.FAMILY, Fonts.SIZE_NORMAL),
            **SegmentedButtonStyles.DEFAULT
        )
        ui_lang_selector.pack(fill="x", pady=(0, Spacing.XXL))
        
        if ui_lang == "english":
            ui_lang_selector.set(self.translations.get("english", ui_lang))
        else:
            ui_lang_selector.set(self.translations.get("russian", ui_lang))
        
        buttons_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=Spacing.XXL, pady=(0, Spacing.XXL))
        
        close_button = ctk.CTkButton(
            buttons_frame,
            text=self.translations.get("close_button", ui_lang),
            command=self.window.destroy,
            height=45,
            font=(Fonts.FAMILY, Fonts.SIZE_MEDIUM, "bold"),
            **ButtonStyles.PRIMARY
        )
        close_button.pack(fill="x")
    
    def change_ui_language(self, value):
        ui_lang = self.settings.get("ui_language")
        
        if value == self.translations.get("english", ui_lang):
            self.settings.set("ui_language", "english")
        else:
            self.settings.set("ui_language", "russian")
        
        self.on_language_change()
        
        if self.window is not None and self.window.winfo_exists():
            self.window.destroy()
