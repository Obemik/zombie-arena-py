from data.config import ARENA_WIDTH, ARENA_HEIGHT, SHOP_ITEMS


class ConsoleRenderer:
    def render(self, engine):
        print("\n" * 3)
        state = engine.state.get_name()
        if state == "playing" or state == "paused":
            self._render_arena(engine)
            self._render_hud(engine)
            self._render_log(engine)
            if state == "paused":
                print("  [ПАУЗА] Натисни P щоб продовжити")
        elif state == "shop":
            self._render_shop(engine)
        elif state == "game_over":
            self._render_game_over(engine)

    def _render_arena(self, engine):
        grid = [["." for _ in range(ARENA_WIDTH)] for _ in range(ARENA_HEIGHT)]
        p = engine.player
        grid[p.position.y][p.position.x] = "@"
        for enemy in engine.enemies:
            x, y = enemy.position.x, enemy.position.y
            grid[y][x] = "Z"
        border = "+" + "-" * ARENA_WIDTH + "+"
        print(border)
        for row in grid:
            print("|" + "".join(row) + "|")
        print(border)

    def _render_hud(self, engine):
        p = engine.player
        bar_len = 20
        filled = int(bar_len * p.hp / p.max_hp)
        bar = "[" + "#" * filled + "-" * (bar_len - filled) + "]"
        weapon_name = p.weapon.name if p.weapon else "Кулаки"
        print("  HP: " + bar + " " + str(p.hp) + "/" + str(p.max_hp) + "   Монети: " + str(p.money) + "   Рахунок: " + str(engine.score))
        print("  Зброя: " + weapon_name + "   Хвиля: " + str(engine.wave) + "   Ворогів: " + str(len(engine.enemies)))
        print("  Рух: w/a/s/d   Атака: E   Пауза: P")

    def _render_log(self, engine):
        print()
        for line in engine.bus.get_log():
            print("  > " + line)

    def _render_shop(self, engine):
        print("  МАГАЗИН")
        print("  Монети: " + str(engine.player.money))
        print()
        for i, item in enumerate(SHOP_ITEMS):
            if i == engine.shop_cursor:
                cursor = "->"
            else:
                cursor = "  "
            print("  " + cursor + " " + item["name"] + "  (" + str(item["cost"]) + " монет)  " + item["desc"])
        print()
        print("  W/S щоб вибрати, E щоб купити, Q щоб продовжити гру")

    def _render_game_over(self, engine):
        print()
        print("  ГРА ЗАКІНЧЕНА")
        print("  Рахунок: " + str(engine.score))
        print("  Хвиля: " + str(engine.wave))
        print()
        print("  Натисни Q для виходу")