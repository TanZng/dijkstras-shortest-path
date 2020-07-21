# Dijkstra's shortest path algorithm 

[![license](https://img.shields.io/github/license/TanZng/dijkstras-shortest-path?color=BLUE&style=for-the-badge)](https://github.com/TanZng/dijkstras-shortest-path/blob/master/LICENSE.md)
[![love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-9cf?style=for-the-badge&logo)](tanx.dev)
[![flask](https://img.shields.io/badge/AND%20-FLASK-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/en/1.1.x/)
[![Progress](https://progress-bar.dev/38/)](https://github.com/TanZng/dijkstras-shortest-path/blob/master/README.md#to-do)

Simple (really simple) web application that plots the shortest path obtained from the Dijkstra's algorithm.

<img src="https://github.com/TanZng/dijkstras-shortest-path/blob/master/flaskr/static/img/node.png " alt="node_icon" width="200"/>


# Table of Contents

- [Table of Contents](#table-of-contents)
	- [Install🚀](#install)
	- [About🤔](#about)
	- [To mess around you need 🛠](#to-mess-around-you-need)
	- [To do📝](#to-do)
   - [Contributing🤝🏼](#contributing)
   - [The Team🙌🏼](#the-team)
   - [License📄](#license)

## Install🚀

1. Fork and clone the Dijkstra's shortest path repo

   ```
   git clone https://github.com/TanZng/dijkstras-shortest-path.git
   ```

2. Create your virtualenv on the proyect root

   ```
   virtualenv flask_env
   ```
  
3. Activate virtualenv/Windows
   ``` Shell
   # Windows
   cd flask_env/Scripts
   activate
   ```
   ``` Bash
   # MacOS, Ubuntu, Debian
   cd flask_env/bin
   source activate
   ```
   
> To leave virtualenv we use ```deactivate```

4. Run Flask App

   ```
   cd flaskr/
   python app.py
   ```

5. Open the direction http://127.0.0.1:5000/ on your browser! 🥳

## About🤔

WIP (Work in Progress)

## To mess around you need🛠

**Git** 

**Python 3** 

I'm using 3.8.3rc1, but i think > 3.4 its okay

**pip** 

To download other dependencies. I'm using pip 20.1.1

```
python -m pip install --upgrade pip
```

**Pandas**

I'm using 1.0.5

```
pip install pandas
```

**Flask**

I'm at 1.1.2

```
pip install Flask
```

**NetworkX**
```
pip install networkx
```

**Plotly**

```
pip install plotly==4.9.0
```
**virtualenv**

```
pip install virtualenv
```

## To do📝
- [x] Load and Read graphs on txt files.
- [x] Render different graphs from a file.
- [x] Set a default example.
- [x] Form to choose u (star) and v (end).
- [x] Create a simple README.md
- [ ] Render shortest path - edge trace - with a diferent color.
- [ ] Upload Dijkstra's shortest path algorithm.
- [ ] Upload the web app.
- [ ] Add "How to use" on the README.
- [ ] Add simple CONTRIBUTING.md
- [ ] Make it responsive.
- [ ] Add CSS Style.
- [ ] Write a Post about this.

## Contributing🤝🏼

Feel free to contribute. I am open to suggestion. Feel free to create an `issue` or open a `PR`

WIP (Work in Progress)

>Please read [CONTRIBUTING.md](link) for details of our code of conduct, and the process to send us pull requests.

## The Team🙌🏼

Tania R. Zuñiga -  Initial Work - [TanZng](https://github.com/TanZng)

<a href="https://www.flaticon.es/autores/becris" title="Becris">Becris</a> Icon designer

## License📄

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://tanx.dev" target="_blank">Tania R Zuniga</a>.
