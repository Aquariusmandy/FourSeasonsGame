﻿#メインメニューの音楽
define config.main_menu_music = "audio/main_theme.mp3"

# セリフテキストボックスの定義。20は左右上下の余白
style narration_window:
    background Frame("gui/narration_window.png", 20, 20)
style vanta_window:
    background Frame("gui/ui_dialoguebox_vanta.png", 20, 20)
style wilson_window:
    background Frame("gui/ui_dialoguebox_wilson.png", 20, 20)
style zali_window:
    background Frame("gui/ui_dialoguebox_zali.png", 20, 20)
style npc_window:
    background Frame("gui/ui_dialoguebox_npc.png", 20, 20)
style vandw_window:
    background Frame("gui/ui_dialoguebox_v&w.png", 20, 20)
style vandc_window:
    background Frame("gui/ui_dialoguebox_crew.png", 20, 20)

# ネームボックスの定義
style vanta_namebox:
    background "gui/ui_namebox_vanta.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style wilson_namebox:
    background "gui/ui_namebox_wilson.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style zali_namebox:
    background "gui/ui_namebox_zali.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style vandw_namebox:
    background "gui/ui_namebox_v&w.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style vandc_namebox:
    background "gui/ui_namebox_v&c.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc01_namebox:
    background "gui/ui_namebox_npc01.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc02_namebox:
    background "gui/ui_namebox_npc02.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc03_namebox:
    background "gui/ui_namebox_npc03.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc04_namebox:
    background "gui/ui_namebox_npc04.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc05_namebox:
    background "gui/ui_namebox_npc05.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

style npc06_namebox:
    background "gui/ui_namebox_npc06.png"
    xalign 0.135
    xoffset 2 # これはピクセル単位での指定です。
    yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
    yoffset -285  # ネームボックスをピクセル単位で上に移動させる

# キャラクター定義
define vanta_char = Character("", color="#ffffff", window_style='vanta_window', namebox_style="vanta_namebox")
define wilson_char = Character("", color="#ffffff", window_style='wilson_window', namebox_style="wilson_namebox")
define zali_char = Character("", color="#ffffff", window_style='zali_window', namebox_style="zali_namebox")
define vandw_char = Character("", color="#ffffff", window_style='vandw_window', namebox_style="vandw_namebox")
define vandc_char = Character("", color="#ffffff", window_style='vandc_window', namebox_style="vandc_namebox")
define npc1_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc01_namebox")
define npc2_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc02_namebox")
define npc3_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc03_namebox")
define npc4_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc04_namebox")
define npc5_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc05_namebox")
define npc6_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc06_namebox")

# キャラクター画像の定義
init:
    image van_sum_nor = "images/chara/van_sum_nor.png"
    image van_sum_thi = "images/chara/van_sum_thi.png"
    image van_sum_ser = "images/chara/van_sum_ser.png"
    image van_sum_hap = "images/chara/van_sum_hap.png"
    image van_sum_sur = "images/chara/van_sum_sur.png"
    image van_sum_emb = "images/chara/van_sum_emb.png"
    image van_sum_con = "images/chara/van_sum_con.png"

    image van_ci_nor = "images/chara/van_ci_nor.png"

    image wil_ci_nor = "images/chara/wil_ci_nor.png"

    image zal_ci_nor = "images/chara/zal_ci_nor.png"

    image van_hr_nor = "images/chara/van_hr_nor.png"
    image van_hr_thi = "images/chara/van_hr_thi.png"
    image van_hr_ser = "images/chara/van_hr_ser.png"
    image van_hr_hap = "images/chara/van_hr_hap.png"
    image van_hr_sur = "images/chara/van_hr_sur.png"
    image van_hr_emb = "images/chara/van_hr_emb.png"
    image van_hr_con = "images/chara/van_hr_con.png"

    image wil_hr_nor = "images/chara/wil_hr_nor.png"

    image zal_hr_nor = "images/chara/zal_hr_nor.png"

    image crew1_nor_img = "images/chara/crew1_nor.png"
    image crew3_nor_img = "images/chara/crew3_nor.png"
    image crew3_ang_img = "images/chara/crew3_ang.png"
    image crew3_hap_img = "images/chara/crew3_hap.png"

    image npc1_img = "images/chara/npc_01.png"
    image npc2_img = "images/chara/npc_02.png"
    image npc3_img = "images/chara/npc_03.png"
    image npc4_img = "images/chara/npc_04.png"
    image npc5_img = "images/chara/npc_05.png"
    image npc6_img = "images/chara/npc_06.png"

    image sum_cv_img = "images/cvisual/sum_cv.png"
    image aut_cv_img = "images/cvisual/aut_cv.png"
    image win_cv_img = "images/cvisual/win_cv.png"
    image spr_cv_img = "images/cvisual/spr_cv.png"

    image sum_bg_beach1_img = "images/bg/sum_bg_beach_01.png"
    image sum_bg_beach2_img = "images/bg/sum_bg_beach_02.png"
    image sum_bg_beach3_img = "images/bg/sum_bg_beach_03.png"
    image sum_bg_beach4_img = "images/bg/sum_bg_beach_04.png"
    image sum_bg_shop1_img = "images/bg/sum_bg_shop_01.png"
    image sum_bg_shop2_img = "images/bg/sum_bg_shop_02.png"

    image aut_bg_village1_img = "images/bg/aut_bg_village_01.png"
    image aut_bg_village2_img = "images/bg/aut_bg_village_02.png"
    image aut_bg_forest1_img = "images/bg/aut_bg_forest_01.png"
    image aut_bg_forest2_img = "images/bg/aut_bg_forest_02.png"
    image aut_bg_forest3_img = "images/bg/aut_bg_forest_03.png"

    image win_bg_office1_img = "images/bg/win_bg_office_01.png"
    image win_bg_office2_img = "images/bg/win_bg_office_02.png"
    image win_bg_shop_img = "images/bg/win_bg_shop_01.png"
    image win_bg_park_img = "images/bg/win_bg_park_01.png"
    image win_bg_home_img = "images/bg/win_bg_home_01.png"
    image win_bg_street1_img = "images/bg/win_bg_street_01.png"
    image win_bg_street2_img = "images/bg/win_bg_street_02.png"
    image win_bg_run_img = "images/bg/win_bg_run.png"

    image sum_st_btst_img = "images/still/sum_st_btst.png"
    image sum_st_bten_img = "images/still/sum_st_bten.png"
    image sum_st_fny_img = "images/still/sum_st_fny.png"
    image sum_edcg_img = "images/still/sum_st_edcg.png"

    image aut_st_btst_img = "images/still/aut_st_btst.png"
    image aut_st_bten_img = "images/still/aut_st_bten.png"
    image aut_st_fny_img = "images/still/aut_st_fny.png"
    image aut_edcg_img = "images/still/aut_st_edcg.png"

    image win_st_btst_img = "images/still/win_st_btst.png"
    image win_st_bten_img = "images/still/win_st_bten.png"
    image win_st_fny_img = "images/still/win_st_fny.png"
    image win_edcg_img = "images/still/win_st_edcg.png"

    image com_base_img = "images/comic/com_base.png"

    image sum_com_1_img = "images/comic/sum_com_1.png"
    image sum_com_2_img = "images/comic/sum_com_2.png"
    image sum_com_3_img = "images/comic/sum_com_3.png"
    image sum_com_4_img = "images/comic/sum_com_4.png"
    image sum_com_5_img = "images/comic/sum_com_5.png"
    image sum_com_6_img = "images/comic/sum_com_6.png"
    image sum_com_7_img = "images/comic/sum_com_7.png"

    image aut_com_1_img = "images/comic/aut_com_1.png"
    image aut_com_2_img = "images/comic/aut_com_2.png"
    image aut_com_3_img = "images/comic/aut_com_3.png"
    image aut_com_4_img = "images/comic/aut_com_4.png"
    image aut_com_5_img = "images/comic/aut_com_5.png"
    image aut_com_6_img = "images/comic/aut_com_6.png"
    image aut_com_7_img = "images/comic/aut_com_7.png"
    image aut_com_8_img = "images/comic/aut_com_8.png"

    image win_com_1_img = "images/comic/win_com_1.png"

#キャラクターの立ち位置2人の時
transform left_2p:
    xalign 0.15
    yalign 0.5
transform right_2p:
    xalign 0.85
    yalign 0.5


# 夏のコミックオーバーレイの配置
# 画像を中央より左上に配置するためのtransformを定義
transform sum_com_1_upper:
    xalign 0.2 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_2_upper:
    xalign 0.7 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_3_upper:
    xalign 0.05 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_4_upper:
    xalign 0.25 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.3 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_5_upper:
    xalign 0.95 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_6_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。

transform sum_com_7_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.15 # 中央より上。0.5が中央なので、それより小さな値。

# 秋のコミックオーバーレイの配置
transform aut_com_1_upper:
    xalign 0.05 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_2_upper:
    xalign 0.95 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.4 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_3_upper:
    xalign 0.03 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_4_upper:
    xalign 0.37 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_5_upper:
    xalign 1.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.25 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_6_upper:
    xalign 0.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_7_upper:
    xalign 1.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.15 # 中央より上。0.5が中央なので、それより小さな値。

transform aut_com_8_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.3 # 中央より上。0.5が中央なので、それより小さな値。

# 冬のコミックオーバーレイの配置
transform win_com_1_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。

default last_screen = None
default active_set = "set1"
default active_tab = "tab1"

init python:
    # define items
    class Item:
        def __init__(self, name, idle, hover, locked, background, description):
            self.name = name
            self.idle = idle
            self.hover = hover
            self.locked = locked
            self.background = background
            self.description = description

    # init items
    croissant = Item("croissant", 
                        "images/UI_inventory/item/btn/btn_croissant_default.png",
                        "images/UI_inventory/item/btn/btn_croissant_hover.png",
                        "images/UI_inventory/item/btn/btn_croissant_locked.png",
                        "frame_walkietalkie.png", #Croissant doesn't have this?
                        "You bought this keychain because it reminded you of Zali's love for quasos.")

    drink = Item("drink", 
                        "images/UI_inventory/item/btn/btn_drink_default.png",
                        "images/UI_inventory/item/btn/btn_drink_hover.png",
                        "images/UI_inventory/item/btn/btn_drink_locked.png",
                        "frame_drink.png", 
                        "You purchased this sparkling drink, and it reminded you of Uki's mysterious eyes. You put the drink in the fridge in A.S.H.'s lab.")

    takoyaki = Item("takoyaki", 
                        "images/UI_inventory/item/btn/btn_takoyaki_default.png",
                        "images/UI_inventory/item/btn/btn_takoyaki_hover.png",
                        "images/UI_inventory/item/btn/btn_takoyaki_locked.png",
                        "frame_takoyaki.png", 
                        "The girl you saved gave you some takoyaki after the fight, they tasted yummy but you wonder where the ingredients came from. ")

    walkietalkie = Item("walkietalkie", 
                        "images/UI_inventory/item/btn/btn_walkietalkie_default.png",
                        "images/UI_inventory/item/btn/btn_walkietalkie_hover.png",
                        "images/UI_inventory/item/btn/btn_walkietalkie_locked.png",
                        "frame_walkietalkie.png", 
                        "A talkie-walkie or a walkie-talkie, THAT is the question. Over.")
    
    mushroom = Item("mushroom", 
                    "images/UI_inventory/item/btn/btn_mushroom_default.png",
                    "images/UI_inventory/item/btn/btn_mushroom_hover.png",
                    "images/UI_inventory/item/btn/btn_mushroom_locked.png",
                    "frame_mushroom.png", 
                    "The mushrooms you picked up on the mountain exude an intriguing scent and boast a surprisingly pleasant flavor, leaving you puzzled yet delighted by their familiar taste.")

    mapleleaf = Item("mapleleaf", 
                    "images/UI_inventory/item/btn/btn_mapleleaf_default.png",
                    "images/UI_inventory/item/btn/btn_mapleleaf_hover.png",
                    "images/UI_inventory/item/btn/btn_mapleleaf_locked.png",
                    "frame_mapleleaf.png", 
                    "A gift from the grateful villagers, crafted locally with the utmost care. Its exquisite aroma tantalizes the senses, promising a sweet indulgence unparalleled by any other maple syrup aficionado.")    

    # try to use achievement to implement the "lock item" function
    achievement.register('croissant')
    achievement.register('drink')
    achievement.register('takoyaki')
    achievement.register('walkietalkie')
    achievement.register('mushroom')
    achievement.register('mapleleaf')


    # obtain items
    def unlock_item(item):
        item.unlocked = True

    def get_item_description(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["description"]
        except KeyError:
            return "Description not available"
    def get_item_background(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["background"]
        except KeyError:
            return "Background not available"
    def get_item_name(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["name"]
        except KeyError:
            return "Name not available"

    def get_item_locked(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["locked"]
        except KeyError:
            return "Name not available"

    image_button_images = {
        "set1": {
            "tab1": [
                {"name": croissant.name, "idle": croissant.idle, "hover": croissant.hover, "locked": croissant.locked, "background":croissant.background,"description":croissant.description},
                {"name": drink.name, "idle": drink.idle, "hover": drink.hover, "locked": drink.locked, "background":drink.background,"description":drink.description},
                {"name": takoyaki.name, "idle": takoyaki.idle, "hover": takoyaki.hover, "locked": takoyaki.locked, "background":takoyaki.background,"description":takoyaki.description},
                {"name": walkietalkie.name, "idle": walkietalkie.idle, "hover": walkietalkie.hover, "locked":walkietalkie.locked,"background":walkietalkie.background,"description": walkietalkie.description},
                {"name": mushroom.name, "idle": mushroom.idle, "hover": mushroom.hover , "locked":mushroom.locked, "background":mushroom.background,"description": mushroom.description},
                {"name": mapleleaf.name, "idle": mapleleaf.idle, "hover": mapleleaf.hover , "locked":mapleleaf.locked, "background":mapleleaf.background,"description": mapleleaf.description},
                {"name": croissant.name, "idle": croissant.idle, "hover": croissant.hover, "locked": croissant.locked, "background":croissant.background,"description":"This is item 7"},
                {"name": drink.name, "idle": drink.idle, "hover": drink.hover, "locked": drink.locked, "background":drink.background,"description":"This is item 8"},
                {"name": takoyaki.name, "idle": takoyaki.idle, "hover": takoyaki.hover, "locked": takoyaki.locked, "background":takoyaki.background,"description":"This is item 9"},
                {"name": walkietalkie.name, "idle": walkietalkie.idle, "hover": walkietalkie.hover, "locked":walkietalkie.locked,"background":walkietalkie.background,"description": "This is item 10"},
                {"name": mushroom.name, "idle": mushroom.idle, "hover": mushroom.hover , "locked":mushroom.locked, "background":mushroom.background,"description": "This is item 11"},
                {"name": mapleleaf.name, "idle": mapleleaf.idle, "hover": mapleleaf.hover , "locked":mapleleaf.locked, "background":mapleleaf.background,"description": "This is item 12"},
                {"name": croissant.name, "idle": croissant.idle, "hover": croissant.hover, "locked": croissant.locked, "background":croissant.background,"description":"This is item 13"},
                {"name": drink.name, "idle": drink.idle, "hover": drink.hover, "locked": drink.locked, "background":drink.background,"description":"This is item 14"},
                {"name": takoyaki.name, "idle": takoyaki.idle, "hover": takoyaki.hover, "locked": takoyaki.locked, "background":takoyaki.background,"description":"This is item 15"},
            ],
            "tab2": [
                {"idle": "6.png", "hover": "5.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 4 description"},
            ],
            # Add images for other tabs in set1 here
        },
        "gallery": {
            "tab1": [
                {"idle": "5.png", "hover": "4.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 4 description"},
            ],
            "tab2": [
                {"idle": "4.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            "tab3": [
                {"idle": "4.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            "tab4": [
                {"idle": "4.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            # Add images for other tabs in gallery here
        },
        "cg": {
            "tab1": [
                {"idle": "6.png", "hover": "4.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            "tab2": [
                {"idle": "5.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            "tab3": [
                {"idle": "5.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            "tab4": [
                {"idle": "5.png", "hover": "6.png", "description": "Item 1 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 2 description"},
                {"idle": "6.png", "hover": "5.png", "description": "Item 3 description"},
            ],
            # Add images for other tabs in cg here
        }
    }




label start:
    # init items
    # $ walkietalkie = Item("walkietalkie", "btn_croissant_default.png","aut_it_walkietalkie.png","frame_walkietalkie.png", "A talkie-walkie or a walkie-talkie, THAT is the question. Over.",False)
    # item2 = Item("", "item2.png", "這是物品2的描述")

    stop music fadeout 1.0  # Fade out menu music
    play music "audio/aut/aut_bgm_03.mp3" loop fadein 1.0  #Loop playback of peaceful songs with fade-in

    show aut_cv_img
    # Wait until the user clicks
    pause

    scene aut_bg_village1_img
    with fade
    play sound "audio/aut/aut_se_bird.mp3" #birdcall

    window hide

    "Krisis has been deployed on a new assignment. You, Zali and Wilson embark on the mission. After a short travel, you arrive at your destination. It's a quiet, cozy village located in the mountains."
    "The village leader is expecting you upon your arrival."
    show npc4_img at center
    npc4_char "Welcome to the village, you must be Krisis! I am so glad you came quickly. I am the leader of this village."
    hide npc4_img
    show van_ci_nor at center
    stop sound fadeout 3.0 #Stop sound effects
    vanta_char "Of course! We need no introduction. But regardless, my name is Vantacrow Bringer. Here to save you all."
    show zal_ci_nor at left
    zali_char "It's our pleasure to meet you. I am Vezalius Bandage, the medic hero of our team Krisis."
    show wil_ci_nor at right
    wilson_char "We come when you call! I'm Yu Q. Wilson, the most talented hero of our team."
    zali_char "Um, anyway, this is a lovely village."
    hide wil_ci_nor
    hide van_ci_nor
    hide zal_ci_nor
    show npc4_img at center
    npc4_char "It's the best time of the year to visit, look at how beautiful the mountains are!"
    scene aut_bg_village2_img
    with fade
    play sound "audio/aut/aut_se_leaves_01.mp3" #The sound of walking on fallen leaves
    "As you discuss the details of the mission, the village leader guides you to the town hall."
    show npc4_img at left_2p
    show van_ci_nor at right_2p
    npc4_char "Our village has always had a good mushroom business. However, this year we have a big quota to fill. So, we decided to venture further up the mountains."
    stop sound fadeout 3.0 #Stop sound effects
    npc4_char "While the team was foraging the mushrooms, they were attacked by some oddly aggressive bears, which had never happened before."
    hide van_ci_nor
    show zal_ci_nor at right_2p
    zali_char "Gosh! That is terrible! Was anyone hurt?"
    npc4_char "Yes, there were some injuries, a few were spooked by the bears. They are resting in the infirmary over there."
    "The village leader points to a door across the room."
    hide zal_ci_nor
    show wil_ci_nor at right_2p
    wilson_char "You can trust Zali! They will be in good hands."
    hide wil_ci_nor
    show zal_ci_nor at right_2p
    zali_char "Alright! You can count on us."
    hide zal_ci_nor
    show van_ci_nor at right_2p
    vanta_char "Let's get ready and head out before it gets dark. We need to investigate."
    hide van_ci_nor
    hide npc4_img

    scene black
    with fade
    scene aut_bg_village1_img
    with fade
    show wil_hr_nor at right
    show van_hr_nor at left
    play sound "audio/aut/aut_se_clothes.mp3" #Change into a hero costume
    "You all decide to gear up for the mission. Meanwhile, you spot Wilson slip a taser gun in his belt.You raise your eyebrow and stare at him."
    vanta_char "You're not bringing your sword? Feeling confident?"
    wilson_char "It's just a bear, there's no job I can't do!"
    vanta_char "Look, I'm just saying, what if—"
    show zal_hr_nor at center
    zali_char "Alright alright! Come on guys, let's focus on the mission! hahaha"
    "Zali interrupts you and Wilson as he tosses you two walkie talkies.\nYou catch them and pass one to Wilson."

    #unlocked item
    $ achievement.grant('walkietalkie')
    if achievement.has('walkietalkie'):
        "Debug message: We got walkietalkie"
    else:
        "We failed"

    zali_char "I'll stay behind and look after the people who were attacked."
    zali_char "Be careful, don't die—if you do, then I can't heal you."
    "You give Zali a quick nod as he heads to the infirmary. You and Wilson turn towards the mountains."
    play sound "audio/aut/aut_se_leaves_01.mp3" #The sound of walking on fallen leaves
    scene aut_bg_forest1_img
    with fade
    "You and Wilson hike along the path, taking in the scenery around you."
    "Everything is breathtaking—from the towering trees, to the crunching of the leaves underfoot, to the crisp autumn air."
    stop sound fadeout 3.0 #Stop sound effects
    show wil_hr_nor at right
    show van_hr_nor at left
    "You take a deep breath."
    vanta_char "The air is so fresh today. I love this time of year."
    wilson_char "Yeah. You are right, this is so beautiful."
    wilson_char "Do you remember that time we went to a forest to hunt down Bigfoot with Alban and Fulgur? You were princess carried the whole way during the mission? That was actually so funny. Ah-hahahah."
    wilson_char "Oh! And we had a group pee together! Actually, I don't want to be reminded of how Fulgur slapped my ass."
    vanta_char "Hmm, hold on...What's that smell?"
    "The scent is familiar, it's something earthy."
    "Intrigued by the smell, you want to find out where it comes from."
    scene aut_bg_forest2_img
    with dissolve
    "You head off the path, and Wilson's yapping voice slowly fades behind you."
    play sound "audio/aut/aut_se_leaves_01.mp3" #The sound of walking on fallen leaves
    show van_hr_nor at center
    "After a few minutes of walking, you find a cluster of amethyst-colored mushrooms."
    stop sound fadeout 3.0 #Stop sound effects
    "You pick one up and—"
    menu:
        "Give it a sniff.":
            "You give it a sniff, and decide that it's too risky to keep it. You drop the mushroom where you found them. "
            jump aut_cho01_accepted
        "Take a small bite.":
            vanta_char "Hmm, the taste is familiar, I wish I could remember where I had it."
            vanta_char "I like it though, I should grab some more! "
            "You grab a few more mushrooms, and put them in your pouch."
            # unlock mushroom
            $ achievement.grant('mushroom')
            if achievement.has('mushroom'):
                "Debug message: We got mushroom"
            else:
                "We failed"
            jump aut_cho01_accepted
    label aut_cho01_accepted:

    "Looking around, you don't recongize your surroundings."
    "You try to find the path you came from, but you can't see it. Yeah...you're lost."
    "Realizing that you left Wilson behind; you take out your walkie talkie and turn it on."
    play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
    show aut_bg_forest3_img
    show van_hr_nor at left
    show wil_hr_nor at right
    wilson_char "Hello? Hello? Can you hear me? This is Wilson speaking. Over."
    wilson_char "Mr. Bringer, do you copy? Over."
    vanta_char "Hello? Wilson? This is Vantacrow Bringer. Over."
    vanta_char "You see, there is this small situation I am in. I may or may not be lost, I'm not sure where I am. Over."
    wilson_char "Vanta, Vanta, Vanta...I look away for 10 seconds and you are gone. Over."
    wilson_char "Tell me what you can see. Over."
    "You look around, and you answer confidently—"
    menu:
        "I'm under a cloud.":
            "The talkie walkie goes silent, is it broken?"
            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            "Then a burst of laughter erupts from the walkie talkie."
            wilson_char "Hahaha... Vanta, you are so stupid!"
            wilson_char "Just stay still, and I will find you. Over"
            vanta_char "Bro, I know this sounds insane, but the cloud I am under actually looks like tentapod! Over."
            wilson_char "Hey Bro...This also sounds insane, but I know exactly where you are, I can see the tentapod cloud, too! Over."
            "Miraculously, against all odds, Wilson manages to track you down with nothing more than a vague description of a cloud's shape."
            hide aut_bg_forest3_img
            with dissolve
            jump aut_cho02_accepted

        "I am surrounded by ​​flowers.":
            wilson_char "Vanta, you do know that doesn't tell me anything. There must be something else around you. Over."
            wilson_char "Can you maybe try to get to higher ground for a good vantage point? haha"
            wilson_char "Try to find a huge rock or a tall tree to climb for a better view. Let me know what you see. Over."
            vanta_char "Wilson! Don't laugh at my pain. Alright, I can see a huge tree. I'm going to climb up the tree and take a look. Over."

            play sound "audio/aut/aut_se_tree.mp3" #The sound of swaying trees
            "As you climb up the tree, you reach for a sturdy branch, inadvertently shaking it."
            "Suddenly, a bee hive plummets to the forest floor; you don't feel very good about this."
            vanta_char "ARE YOU SERIOUS? PINEAPPLES!"
            "Yes, we are serious."

            play sound "audio/aut/aut_se_wasp.mp3" #buzz of a bee
            "The air fills with buzzing as hundreds of bees swarm around, seeking the source of the disturbance to their home."
            "You are so distraught you can't hear Wilson calling for you from the walkie talkie."
            vanta_char "Oh shittake mushroom—"
            vanta_char "Oh please, not like this!!"
            vanta_char "AHHHHHHHHHH!!!"

            play sound "audio/aut/aut_se_tree.mp3" #The sound of swaying trees
            "Panicked, you leap from the tree, but instead of landing in your signature hero pose, you stumble, struggling to maintain your balance."

            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            wilson_char "Vanta? VANTA? Are you okay? Are you there?"
            wilson_char "Answer me! Tell me what's going on! OVER!"
            vanta_char "No No No No No No No! You can't see me! You can't see me! You can't see me!"
            vanta_char "{size=45}WILSON—SHUT UP!!{/size}"
            vanta_char "AHHHHHH!"

            play sound "audio/aut/aut_se_wasp.mp3" #buzz of a bee
            "The enraged bees chase you relentlessly. Your heart races as you sprint through the forest; you weave between trees in a frantic attempt to throw off the bees."

            play sound "audio/aut/aut_se_leaves_02.mp3" #The sound of running on fallen leaves
            "Adrenaline fuels your legs as you push yourself to your limits. Every step is a leap of faith."
            "This is not as easy as fighting a giant octopus, and certainly not feasible for an ordinary human. But you are Vantacrow Bringer, you refuse to be defeated."
            "You don't know how long you've been bolting, the pursuit of the bees gradually fades into the distance."
            "You turn a corner with haste, colliding with something, a flash of yellow blocks your vision. Before you can regain your balance, strong arms wrap around you, lifting you effortlessly off your feet."

            $ renpy.music.set_volume(0.2, delay=2.0, channel='music')  # Take 2 seconds and set the volume to 0.2
            hide aut_bg_forest3_img
            show aut_st_fny_img
            with fade

            play sound "audio/aut/aut_se_syojyo.mp3" #The Sound of Shoujo Manga
            pause 2.0
            "Startled, you find yourself in a princess carry, the unexpected encounter leaving you momentarily breathless as you gaze up into the eyes of..."
            "Yu Q. Wilson."
            wilson_char "Oh I found you!"
            wilson_char "I told you to stay still and don't touch anything, Mr. Vantacrow Bringer."
            wilson_char "Can I let go now? hahaha"
            vanta_char "Wh—How would I know there was a beehive on that tree?!"
            vanta_char "Thanks for the lift."
            $ renpy.music.set_volume(1, channel='music')  # Volume back to maximum (maybe user setting)
            hide aut_st_fny_img
            with fade
            jump aut_cho02_accepted

    label aut_cho02_accepted:

    "The two heroes finally reunite; now they can valiantly press on with their mission."
    play sound "audio/aut/aut_se_leaves_01.mp3" # Sound of walking on leaves
    "Now, you and Wilson are looking for any traces of evidence from the previous attacks. You comb through the bushes, parting leaves and branches to inspect every inch of the forest."
    "You find a suitable location to set up a trap, using the natural resources of the forest to camouflage it seamlessly within the surroundings."
    stop sound fadeout 3.0 # Stop sound with a fadeout
    "There, amidst a vibrant carpet of fallen leaves, a playful cub frolics with joy. The air is filled with the sound of its carefree dance and rustling leaves. You whistle to get Wilson's attention to look at the cub amongst the golden foliage."
    wilson_char "Oh my god, that is sho cyute. Oh! We should make sure it doesn't accidentally get into the trap."
    vanta_char "Oh yeah! I'll grab a leaf to entice the cub away from the trap."
    wilson_char "Oh no, if the cub is here..."
    wilson_char "Then the mama bear must be nearby, we should watch out—"

    play music "audio/sum/sum_bgm_02.mp3" loop fadein 1.0 # Battle music
    play sound "audio/aut/aut_se_bear_01.mp3" # Bear growling sound
    show aut_st_btst_img
    pause 2.0
    "All of a sudden, a low, rumbling growl echoes from behind you."
    "Your heart skips a beat, you turn to face the source of the ominous sound, only to find yourself locking eyes with a bear whose fur bristles with aggression."
    "Ah, just what you need—another item checked off the bucket list: getting chased by a bear. How thrilling!"

    play sound "audio/aut/aut_se_bear_02.mp3" # Bear growling sound
    "The bear lets out a terrifying roar, the forest trembles in response. It exudes unusual agitation and aggression, its abnormally large form far surpassing any bears you've encountered before."
    "You and Wilson pause for a second, exchanging a look that says, 'Deuces!'."

    play sound "audio/aut/aut_se_leaves_02.mp3" # Sound of running on leaves
    "Without saying a word, you read your homie's mind, and simultaneously turn on your heels, racing down the mountain."
    stop sound fadeout 3.0 #効果音を止める
    scene aut_bg_forest2_img
    with dissolve
    show van_hr_nor at left
    show wil_hr_nor at right
    wilson_char "Vanta? That's not just an angry bear!!"
    wilson_char "GO GO GO! I think we should go back to Zali!"
    vanta_char "Ahhh!!  THAT IS HUGE..."
    vanta_char "...That's what she said."
    hide van_hr_nor
    hide wil_hr_nor
    show com_base_img
    show aut_com_1_img at aut_com_1_upper
    vandw_char "AHHHHHHHHH!!!"

    play sound "audio/aut/aut_se_leaves_02.mp3" # Sound of running on leaves
    "You and Wilson rapidly approach the village entrance. You see Zali, his presence a beacon of hope."
    stop sound fadeout 3.0 # Stop sound with a fadeout
    show aut_com_2_img at aut_com_2_upper
    zali_char "What the hell?! What did you guys do?!"
    zali_char "I said not to get hurt, not to surprise me like this!"

    play sound "audio/aut/aut_se_bear_02.mp3" # Bear growling sound
    "The bear catches up to the three of you, slashing towards Wilson."
    "With lightning reflexes, he swiftly dodges to the side, narrowly avoiding the deadly swipe. However, the bear's sheer force collides with a nearby tree, sending it crashing to the ground."
    hide aut_com_1_img
    hide aut_com_2_img
    show aut_com_3_img at aut_com_3_upper
    play sound "audio/sum/sum_se_tako_02.mp3" # Sound of dodging an attack, reused.
    wilson_char "HA! You can't lay a finger on the best former hitman ever—"
    wilson_char "WOAHHHH!! Who put this thing here?!"
    show aut_com_4_img at aut_com_4_upper
    play sound "audio/aut/aut_se_rope.mp3" # Sound of rope
    "As Wilson nimbly dodges the attack, he accidentally triggers a snare trap, finding himself abruptly hoisted upside down."
    zali_char "WILSON! Use your taser gun!"
    # Sound of a taser gun
    show aut_com_5_img at aut_com_5_upper
    play sound "audio/aut/aut_se_taser.mp3"
    "Wilson draws his taser gun from his belt, he skillfully aims and fires at the bear while hanging upside down. To everyone's surprise, the bear is only stunned for a few seconds. It's about to attack again."
    wilson_char "MY GOD! That only stunned the bear, just how strong is this bear?"
    "Seeing Wilson in peril, you quickly assess the situation and leap into action. You rush to Wilson's side and begin to untie the trap, wanting to free him from his precarious predicament."
    hide aut_com_3_img
    hide aut_com_4_img
    hide aut_com_5_img
    show aut_com_6_img at aut_com_6_upper
    vanta_char "Wilson, hang in there!"

    play sound "audio/aut/aut_se_rope.mp3" # Sound of rope
    vanta_char "God damn it. This rope is so fricking tight..."
    "However, you are not fast enough, the bear is about to strike again—"
    zali_char "Vanta! The bear!!!{size=40}Wilson—{/size}"

    play sound "audio/aut/aut_se_bandage.mp3" # Sound of bandages
    "As the bear unleashes another slashing attack on Wilson, strips of Zali's bandages shoot towards the bear's claws, ensnaring its movements and halting its impending strike."
    "The bear's immense strength begins to strain the bandages, causing them to fray as they are pulled."
    "As elegant as Zali has always been, his voice carries a tone of genuine concern for his teammates."
    zali_char "{size=40}I won't let you hurt Wilson!!{/size}"
    zali_char "UGHHHH!! Van..ta!! I can't hold this forever!"
    vanta_char "{size=40}ZALI!!! HANG ON!!! I AM COMING!!{/size}"
    vanta_char "{size=40}Oh that sounds bad, I mean I AM ARRIVING!!{/size}"
    vanta_char "{size=40}...That also sounds bad, forget it. \nI'LL BE THERE IN JUST A SECOND!!{/size}"
    "After freeing Wilson from the trap, you shift your focus to Zali."
    show aut_com_7_img at aut_com_7_upper
    play sound "audio/sum/sum_se_kougeki_01.mp3" # Sound of tackling, reused.
    "With unwavering determination, you leap onto the bear, swiftly wrapping your arms and legs around its massive form. The moment Wilson's skates touch the ground, he propels himself forward, launching into a fierce tackle aimed at the bear."
    vandw_char "{size=45}EUHHHHH AHHHHHH!!! ZALI! RIGHT NOW!!{/size}"
    zali_char "Don't worry, bear. This will be over quickly, and you won't feel a thing."
    hide aut_com_6_img
    hide aut_com_7_img
    show aut_com_8_img at aut_com_8_upper
    play sound "audio/aut/aut_se_needle.mp3" # Sound of needle
    "Zali regains his composure and speaks with a soothing tone. He produces a syringe seemingly out of thin air, and before you can register any movement, the needle is already under the bear's skin."
    "A tube of unknown liquid slowly disappears into the bear's body, as Zali expertly administers the sedative."
    play sound "audio/sum/sum_se_koke.mp3" # Sound of bear collapsing, reused.
    "The bear slumps onto the ground as the tension in the bandages loosens, surrendering to the sedative's effects."
    hide com_base_img
    hide aut_com_8_img
    with dissolve
    "You and Wilson are stunned by the seamless execution of Zali's actions within mere seconds."
    show zal_hr_nor
    zali_char "Alright! This potion can ensure that the bear sleeps peacefully until it goes back to A.S.H."
    zali_char "I will call A.S.H's team to get a case to take the bear back. If there are cubs, I will take care of them, too."
    zali_char "Alright then! Nice, guys! That was quite close. But it all worked out in the end. hahaha"
    stop music fadeout 1.0
    play music "audio/aut/aut_bgm_01.mp3" loop fadein 1.0 # Peaceful music
    show aut_st_bten_img
    with fade
    pause 2.0
    wilson_char "V…Vanta?"
    vanta_char "…Yeah?"
    wilson_char "Did you see what Zali just did?"
    vanta_char "…That he gracefully injected that mysterious syringe to sedate a bear of such size, all without batting an eye?"
    "You and Wilson feel a chill go down your spines."
    "Once again, you can read your homie's mind."
    zali_char "What?\nWhat are you guys chatting about?"
    "Zali looks at the two of you, clearly puzzled, but with a smile adorning his face."
    zali_char "Your faces look weird. Did I do something wrong?"
    vandw_char "{size=50}No-nothing!{/size}"
    scene aut_bg_village1_img
    with fade
    show van_hr_nor at left
    show wil_hr_nor at right
    show zal_hr_nor at center

    "The A.S.H. logistics team arrives at the scene just as the sun begins its descent, bringing with them a customized cage tailored for the bear."
    "As the intense battle finally concludes, the villagers express their appreciation for your efforts by offering a plethora of souvenirs.They give you some locally made maple syrup and a bucket of their specialty mushrooms, each item symbolizing their heartfelt thanks."
    zali_char "These mushrooms look very interesting...They have a unique smell. I want to see what I can do with them."
    "The Three of you also indulge in some delicious mushroom dishes prepared by the villagers, savoring the flavors of their generosity."
    "As peace returns to the mountain, you bid farewell to the villagers, the tranquility of the moment etched in your memory."
    "A single maple leaf gently lands on your shoulder, a poignant reminder that even as you depart, nature itself bids its own farewell to the season."
    show aut_edcg_img
    with fade
    # Display END at the bottom right
    show text "{b}{size=80}END{/size}{/b}" at Position(xalign=0.95, yalign=0.95)
    # Wait for user to click
    pause
    return



