# SpriteSheeter
Configurable sprite sheet generator

## Sample Images

`ImagesPerRow=3`

![alt text](https://github.com/jiinurppa/SpriteSheeter/raw/master/SpriteSheetHorizontal.png "Horizontal Sample Image")

`ImagesPerRow=1`

![alt text](https://github.com/jiinurppa/SpriteSheeter/raw/master/SpriteSheetVertical.png "Vertical Sample Image")

`ImagesPerRow=2`

![alt text](https://github.com/jiinurppa/SpriteSheeter/raw/master/SpriteSheet.png "Grid Sample Image")

## Usage:
Load default configuration file `config.ini`
```bash
SpriteSheeter.py
```
Load configuration file `file.ini`
```bash
SpriteSheeter.py file.ini
```

## Configuration Parameters
See `sample.ini` for a generic example.
| Parameter       | Example         | Description                                     |
| --------------- | --------------- | ----------------------------------------------- |
| OutputFormat    | PNG             | Format for writing sprite sheet                 |
| OutputFilename  | SpriteSheet.png | Sprite sheet file name                          |
| BackgroundColor | White           | Background color (hex/name)                     |
| BackgroundAlpha | 0               | Background alpha (0-255)                        |
| ImagesPerRow    | 2               | How many sprites per row (see sample images)    |
| DrawOrder       | file.png        | Drawing order of images (files can be repeated) |
