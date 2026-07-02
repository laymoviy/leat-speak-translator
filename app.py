import customtkinter as ctk
from tkinter import END
from leet_generator import LeetSpeakGenerator
from translations import Translations
from settings import Settings
from settings_window import SettingsWindow
from styles import (
    Colors, Fonts, Spacing, BorderRadius,
    ButtonStyles, FrameStyles, TextboxStyles,
    LabelStyles, WindowStyles
)

class LeetSpeakApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("1100x750")
        self.window.minsize(900, 650)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.generator = LeetSpeakGenerator()
        self.translations = Translations()
        self.settings = Settings()
        self.settings_window = SettingsWindow(
            self.window, 
            self.settings, 
            self.translations, 
            self.update_texts
        )
        
        self.setup_ui()
        self.update_texts()
        
    def setup_ui(self):
        self.window.configure(**WindowStyles.MAIN)
        
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        
        header_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent",
            height=100
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=Spacing.XXL, pady=(Spacing.XXL, Spacing.LG))
        header_frame.grid_columnconfigure(0, weight=1)
        
        title_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_container.grid(row=0, column=0, sticky="w")
        
        icon_label = ctk.CTkLabel(
            title_container,
            text="⚡",
            font=(Fonts.FAMILY, 36),
            text_color=Colors.PRIMARY
        )
        icon_label.pack(side="left", padx=(0, Spacing.MD))
        
        self.title_label = ctk.CTkLabel(
            title_container,
            text="",
            font=(Fonts.FAMILY, Fonts.SIZE_TITLE, "bold"),
            text_color=Colors.TEXT_PRIMARY
        )
        self.title_label.pack(side="left")
        
        self.settings_button = ctk.CTkButton(
            header_frame,
            text="⚙",
            width=50,
            height=50,
            command=self.settings_window.open,
            font=(Fonts.FAMILY, 24),
            **ButtonStyles.GHOST
        )
        self.settings_button.grid(row=0, column=1, padx=(Spacing.MD, 0))
        
        content_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        content_frame.grid(row=2, column=0, sticky="nsew", padx=Spacing.XXL, pady=(0, Spacing.LG))
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        left_card = ctk.CTkFrame(content_frame, **FrameStyles.CARD)
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, Spacing.MD))
        left_card.grid_rowconfigure(1, weight=1)
        left_card.grid_columnconfigure(0, weight=1)
        
        left_header = ctk.CTkFrame(left_card, fg_color="transparent")
        left_header.grid(row=0, column=0, sticky="ew", padx=Spacing.XL, pady=(Spacing.XL, Spacing.MD))
        
        self.left_label = ctk.CTkLabel(
            left_header,
            text="",
            font=(Fonts.FAMILY, Fonts.SIZE_LARGE, "bold"),
            text_color=Colors.TEXT_PRIMARY
        )
        self.left_label.pack(side="left")
        
        char_count_frame_left = ctk.CTkFrame(left_header, fg_color="transparent")
        char_count_frame_left.pack(side="right")
        
        self.input_char_count = ctk.CTkLabel(
            char_count_frame_left,
            text="0",
            font=(Fonts.FAMILY, Fonts.SIZE_SMALL),
            text_color=Colors.TEXT_SECONDARY
        )
        self.input_char_count.pack()
        
        self.input_text = ctk.CTkTextbox(
            left_card,
            font=(Fonts.FAMILY_MONO, Fonts.SIZE_MEDIUM),
            wrap="word",
            **TextboxStyles.DEFAULT
        )
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=Spacing.XL, pady=(0, Spacing.XL))
        self.input_text.bind("<KeyRelease>", self.on_text_change)
        
        right_card = ctk.CTkFrame(content_frame, **FrameStyles.CARD)
        right_card.grid(row=0, column=1, sticky="nsew", padx=(Spacing.MD, 0))
        right_card.grid_rowconfigure(1, weight=1)
        right_card.grid_columnconfigure(0, weight=1)
        
        right_header = ctk.CTkFrame(right_card, fg_color="transparent")
        right_header.grid(row=0, column=0, sticky="ew", padx=Spacing.XL, pady=(Spacing.XL, Spacing.MD))
        
        leet_icon = ctk.CTkLabel(
            right_header,
            text="🔥",
            font=(Fonts.FAMILY, 18)
        )
        leet_icon.pack(side="left", padx=(0, Spacing.SM))
        
        self.right_label = ctk.CTkLabel(
            right_header,
            text="",
            font=(Fonts.FAMILY, Fonts.SIZE_LARGE, "bold"),
            text_color=Colors.PRIMARY
        )
        self.right_label.pack(side="left")
        
        char_count_frame_right = ctk.CTkFrame(right_header, fg_color="transparent")
        char_count_frame_right.pack(side="right")
        
        self.output_char_count = ctk.CTkLabel(
            char_count_frame_right,
            text="0",
            font=(Fonts.FAMILY, Fonts.SIZE_SMALL),
            text_color=Colors.TEXT_SECONDARY
        )
        self.output_char_count.pack()
        
        self.output_text = ctk.CTkTextbox(
            right_card,
            font=(Fonts.FAMILY_MONO, Fonts.SIZE_MEDIUM),
            wrap="word",
            state="disabled",
            **TextboxStyles.DEFAULT
        )
        self.output_text.grid(row=1, column=0, sticky="nsew", padx=Spacing.XL, pady=(0, Spacing.XL))
        
        actions_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )
        actions_frame.grid(row=3, column=0, sticky="ew", padx=Spacing.XXL, pady=(Spacing.LG, Spacing.XL))
        
        buttons_container = ctk.CTkFrame(actions_frame, fg_color="transparent")
        buttons_container.pack(side="left")
        
        self.copy_button = ctk.CTkButton(
            buttons_container,
            text="",
            command=self.copy_leet_text,
            width=180,
            height=45,
            font=(Fonts.FAMILY, Fonts.SIZE_MEDIUM, "bold"),
            **ButtonStyles.PRIMARY
        )
        self.copy_button.pack(side="left", padx=(0, Spacing.MD))
        
        self.clear_button = ctk.CTkButton(
            buttons_container,
            text="",
            command=self.clear_text,
            width=140,
            height=45,
            font=(Fonts.FAMILY, Fonts.SIZE_MEDIUM),
            **ButtonStyles.OUTLINE
        )
        self.clear_button.pack(side="left")
        
        footer_frame = ctk.CTkFrame(actions_frame, fg_color="transparent")
        footer_frame.pack(side="right")
        
        version_label = ctk.CTkLabel(
            footer_frame,
            text="v1.0",
            font=(Fonts.FAMILY, Fonts.SIZE_SMALL),
            text_color=Colors.TEXT_DISABLED
        )
        version_label.pack(side="right", padx=(Spacing.SM, 0))
        
        separator = ctk.CTkLabel(
            footer_frame,
            text="•",
            font=(Fonts.FAMILY, Fonts.SIZE_SMALL),
            text_color=Colors.TEXT_DISABLED
        )
        separator.pack(side="right", padx=Spacing.SM)
        
        made_with_label = ctk.CTkLabel(
            footer_frame,
            text="Made by laymoviy",
            font=(Fonts.FAMILY, Fonts.SIZE_SMALL),
            text_color=Colors.TEXT_DISABLED
        )
        made_with_label.pack(side="right")
    
    def update_texts(self):
        ui_lang = self.settings.get("ui_language")
        
        self.window.title(self.translations.get("title", ui_lang))
        self.title_label.configure(text=self.translations.get("title", ui_lang))
        self.left_label.configure(text=self.translations.get("input_label", ui_lang))
        self.right_label.configure(text=self.translations.get("output_label", ui_lang))
        self.clear_button.configure(text=self.translations.get("clear_button", ui_lang))
        self.copy_button.configure(text=f"📋 {self.translations.get('copy_button', ui_lang)}")
        
    def on_text_change(self, event=None):
        input_content = self.input_text.get("1.0", END).strip()
        leet_content = self.generator.convert_to_leet(input_content)
        
        self.input_char_count.configure(text=str(len(input_content)))
        self.output_char_count.configure(text=str(len(leet_content)))
        
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", END)
        self.output_text.insert("1.0", leet_content)
        self.output_text.configure(state="disabled")
    
    def clear_text(self):
        self.input_text.delete("1.0", END)
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", END)
        self.output_text.configure(state="disabled")
        self.input_char_count.configure(text="0")
        self.output_char_count.configure(text="0")
    
    def copy_leet_text(self):
        leet_content = self.output_text.get("1.0", END).strip()
        self.window.clipboard_clear()
        self.window.clipboard_append(leet_content)
        
        original_text = self.copy_button.cget("text")
        ui_lang = self.settings.get("ui_language")
        self.copy_button.configure(
            text="✓ Copied!" if ui_lang == "english" else "✓ Скопировано!",
            fg_color=Colors.SUCCESS
        )
        self.window.after(1500, lambda: self.copy_button.configure(
            text=original_text,
            fg_color=ButtonStyles.PRIMARY["fg_color"]
        ))
    
    def run(self):
        self.window.mainloop()
