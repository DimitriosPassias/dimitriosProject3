import arcade

my_window = arcade.open_window(1080, 900, "Bat Insignia")

arcade.set_background_color(arcade.color.DARK_YELLOW)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(600, 650, 500, 300, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(200, 600, 475, 325, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(150, 200, 500, 300, arcade.color.BLACK)
arcade.draw_arc_filled(650, 300, 100, 100, arcade.color.BLACK, -180, -90)
arcade.draw_arc_filled(150, 300, 100, 100, arcade.color.BLACK, -90,0)
arcade.draw_arc_filled(650, 500, 100, 100, arcade.color.BLACK, 90,180)
arcade.draw_arc_filled(150, 500, 100, 100, arcade.color.BLACK, 0,90)
arcade.draw_circle_filled(400, 450, 50, arcade.color.BLACK)
arcade.draw_line(360, 525, 360, 475, arcade.color.BLACK, 10)
arcade.draw_line(440, 525, 440, 475, arcade.color.BLACK, 10)


arcade.draw_triangle_filled(400, 250, 350, 325, 450, 325, arcade.color.BLACK)
arcade.draw_circle_outline(400, 400, 300, arcade.color.BLACK, 10)


signature = arcade.Text("Batman by Dimitrios Passias",700,200, arcade.color.AMAZON, 20)
signature.draw()

arcade.finish_render()

arcade.run()