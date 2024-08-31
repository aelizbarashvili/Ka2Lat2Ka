## Georgian Character Encoding and Processing

All Georgian characters are transformed in 3-byte sequences when Using UTF-8 encoding. Multi-byte characters generally require more resources than one-byte characters. In terms of storage, each multi-byte character typically requires more than one byte to represent, compared to one-byte characters. This means they occupy more storage space. Regarding processing, the CPU must determine the encoding of each character to interpret it correctly. For multi-byte characters, this involves checking multiple bytes, which can be more computationally intensive. In terms of memory, as an application processes more multi-byte characters, it may need to allocate additional memory for temporary data structures or intermediate results. Caching can further consume memory, particularly when dealing with large amounts of multi-byte text.

When working with Georgian texts, it’s common to encounter a mix of Georgian letters along with Latin or other foreign characters. This situation involves handling both single-byte and multi-byte characters simultaneously.

If Georgian characters were one byte, working with text would be less computationally intensive. Our approach to addressing the issue of Georgian character size involves isolating the non-Georgian parts of the text and  transliterating only the Georgian portions of the text while leaving the rest unchanged. To accomplish this, we use a custom translation table along with a marker system. Modern Georgian has 33 letters, so our transliteration table maps these characters to both lowercase and uppercase basic Latin characters. Before applying this table, we first employ markers to identify patterns in the text that contain basic Latin characters, which are part of our transliteration table. This process ensures that non-Georgian characters in the original text remain unchanged, while transliteration and detransliteration are applied only to the unmarked segments. Detransliteration is technically a form of transliteration. It is the reverse process of transliteration. While transliteration converts text from one script to another, detransliteration converts the transliterated text back to its original script.

By mapping each Georgian character to a unique basic Latin equivalent and vice versa, we can achieve a bijective conversion process.

Here are Scripts and Tools for Transliteration and Detransliteration.

* Python scripts (ka2lat.py and lat2kat.py):
  - ka2lat.py script uses a custom translation table (ka2lat) for mapping Georgian to Latin characters.
  - Two parameters, "File" and "Marker" are used to specify the file path and to define symbol for isolating Latin segments.
  - Detransliteration is done the script lat2kat.py using a custom translation table (lat2kat).
  - Low memory usage.

* Sed Command (ka2lat2ka.sed):
  – The a sed command is used for both transliteration and detransliteration.
  – Sed gives best result in detransliteration.
  - Low memory usage.

* Vim text editor (ka2lat2ka.vim):
  – we explored transliteration and detranslation processes using the vim text editor.
  – Vim’s buffer-based processing showed the fastest processing times for transliteration.
  - In contrast, vim shows a significant increase in memory usage as file sizes grow, with sharper rises for larger files.
