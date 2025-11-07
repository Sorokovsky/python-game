from sorok_engine.scene import Scene


def main() -> None:
    scene = Scene()
    scene.create_object((0, 0), (20, 20))
    scene.run()


if __name__ == "__main__":
    main()
