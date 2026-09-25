set(LV_CONF_PATH ${CMAKE_CURRENT_LIST_DIR}/lv_conf.h)

include(${MICROPY_DIR}/../lv_binding/micropython.cmake)

add_library(lvgl_font INTERFACE)
# Remove all error "Too large font or glyphs in FONT_PUHUI_20. Enable LV_FONT_FMT_TXT_LARGE in lv_conf.h"
target_sources(lvgl_font INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/font_puhui_14.c
    ${CMAKE_CURRENT_LIST_DIR}/font_puhui_16.c
    ${CMAKE_CURRENT_LIST_DIR}/font_puhui_20.c
)
target_link_libraries(usermod_lvgl INTERFACE lvgl_font)
