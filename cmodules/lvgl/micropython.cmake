set(LV_CONF_PATH ${CMAKE_CURRENT_LIST_DIR}/lv_conf.h)

include(${MICROPY_DIR}/../lv_binding/micropython.cmake)

# Puhui Fonts from https://github.com/78/xiaozhi-fonts
add_library(usermod_lvgl_font INTERFACE)
target_sources(usermod_lvgl_font INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/font_puhui_14_1.c
    ${CMAKE_CURRENT_LIST_DIR}/font_puhui_16_4.c
)
target_link_libraries(usermod INTERFACE usermod_lvgl_font)
