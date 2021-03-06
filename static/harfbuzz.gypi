{
    'includes': ['common.gypi', 'locations.gypi'],
    'targets': [{
        'target_name': 'hb-ucdn',
        'type': 'static_library',
        'include_dirs': ['<(harfbuzz_root)src/hb-ucdn'],
        'defines': ['HAVE_CONFIG_H'],
        'sources': [
            "<(harfbuzz_root)src/hb-ucdn/ucdn.c"
        ]
    }, {
        'target_name': 'harfbuzz',
        'type': 'static_library',
        'include_dirs': [
            '<(harfbuzz_root)src',
            '<(harfbuzz_root)src/hb-ucdn',
            'custom-include/harfbuzz',

            '<(freetype_root)/include',
            '<(glib_root)',
            '<(glib_root)/glib',
            'custom-include/glib',
        ],
        'dependencies': ['hb-ucdn'],
        'defines': ['HAVE_CONFIG_H'],
        'sources': [
            "<(harfbuzz_root)src/hb-blob.cc",
            "<(harfbuzz_root)src/hb-buffer-serialize.cc",
            "<(harfbuzz_root)src/hb-buffer.cc",
            "<(harfbuzz_root)src/hb-common.cc",
            "<(harfbuzz_root)src/hb-face.cc",
            "<(harfbuzz_root)src/hb-font.cc",
            "<(harfbuzz_root)src/hb-ot-tag.cc",
            "<(harfbuzz_root)src/hb-set.cc",
            "<(harfbuzz_root)src/hb-shape.cc",
            "<(harfbuzz_root)src/hb-shape-plan.cc",
            "<(harfbuzz_root)src/hb-shaper.cc",
            "<(harfbuzz_root)src/hb-unicode.cc",
            "<(harfbuzz_root)src/hb-warning.cc",
            "<(harfbuzz_root)src/hb-ot-font.cc",
            "<(harfbuzz_root)src/hb-ot-layout.cc",
            "<(harfbuzz_root)src/hb-ot-map.cc",
            "<(harfbuzz_root)src/hb-ot-math.cc",
            "<(harfbuzz_root)src/hb-ot-shape.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-arabic.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-default.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-hangul.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-hebrew.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-indic.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-indic-table.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-myanmar.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-thai.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-tibetan.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-use.cc",
            "<(harfbuzz_root)src/hb-ot-shape-complex-use-table.cc",
            "<(harfbuzz_root)src/hb-ot-shape-normalize.cc",
            "<(harfbuzz_root)src/hb-ot-shape-fallback.cc",
            "<(harfbuzz_root)src/hb-ot-var.cc",
            "<(harfbuzz_root)src/hb-fallback-shape.cc",
            "<(harfbuzz_root)src/hb-glib.cc",
            "<(harfbuzz_root)src/hb-ft.cc",
            "<(harfbuzz_root)src/hb-ucdn.cc",
        ]
    }]
}
