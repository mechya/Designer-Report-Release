# Fonts

Reports should use fonts that are available wherever they are compiled and filled. Designer Report therefore uses the fonts in the workspace's **`fonts/` folder** — the font list in the Properties panel shows only these fonts.

## Manage Fonts

**Tools → Manage Fonts** shows the fonts of the workspace.

- **The list** shows each font by its own name — the name used in reports (for example `游ゴシック Medium`, `ＭＳ 明朝`).
- **Preview** — sample Latin, kana and kanji text; change the size with *Size*.
- **Font Info** — details read from the font file: file and size, name (Japanese / English), family, style, version, manufacturer, designer, copyright, trademark and license. The copy button copies them as text.
- **Font collections (.ttc)** contain several fonts (e.g. MS Gothic, MS UI Gothic and MS PGothic). Choose one under *Font in file* to see its details and preview it.
- **Add Font…** copies `.ttf`, `.otf` or `.ttc` files into `fonts/`; **Remove** deletes the selected font; **Open Fonts Folder** opens it in Explorer / Finder.

## Included fonts

Designer Report includes these free fonts, licensed under the SIL Open Font License:

- **Noto Sans JP**, **Noto Serif JP**
- **BIZ UDGothic**, **BIZ UDMincho**

## Font licenses — please check

A font's license decides where you may use it. Check the **License** line in Font Info before you copy a font into a workspace that you share with others or ship with an application.

- Fonts that come with Windows (MS Gothic, MS Mincho, Meiryo, Yu Gothic, Yu Mincho, …) say *"Microsoft supplied font … Any other use is prohibited."* You may use them to create and print documents on a licensed Windows computer, but **not redistribute** them — for example by committing them to a public repository or bundling them with your own application.
- Fonts under the **SIL Open Font License** (Noto, BIZ UD, IPAex, …) may be redistributed and bundled.

## Fonts in compiled reports

**Compile** copies only the fonts the reports actually use into `build/fonts/`, together with their license files and a matching `jasper-fonts.xml`, so the compiled `.jasper` files can be filled on another machine with the same fonts. Fonts nothing refers to are left out, and a font a report asks for but the workspace does not have is reported in the console.
