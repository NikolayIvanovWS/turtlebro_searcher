## Инструкция пакета turtlebro_searcher

Для реализации патрулирования необходимо чтобы на роботе был установлен пакет ```turtlebro_patrol```:
https://github.com/voltbro/turtlebro_patrol

#### Установить пакет ROS 

```
cd ~catkin_ws/src
git clone https://github.com/NikolayIvanovWS/turtlebro_searcher
cd ../
catkin_make --pkg turtlebro_searcher
```

### Запуск пакета

Запуск ноды патрулирования и режима, в которой робот считывает aruco маркеры
```
roslaunch turtlebro_searcher searcher_aruco.launch
```
_Важное примечание!_

Для того, чтобы робот начал считывать aruco маркеры, необходимо переключить работу камеры с веб-интерфейса на публикацию данных в ROS. Подробнее об этом в инструкции: https://manual.turtlebro.ru/paket-turtlebro/video

### Работа пакета

Пакет поисковика реализует запуск ServiceServer, реализующий логику работы "Поисковика" в точках патрулирования.

При запуске ноды патрулирования указывается имя сервиса, который вызывается для реализации логики в точках патрулирования.

```xml
  <!--Patrol Node -->
  <node pkg="turtlebro_patrol" type="patrol.py" name="turtlebro_patrol" output="screen" required="true">
    <param name="waypoints_data_file" value="$(arg waypoints_data_file)"/>    
    <param name="point_callback_service" value="turtlebro_searcher"/>    
  </node>
```  

### Работа с Aruco маркерами

Для реализации работы с маркерами в пакете реализован ServiceServer ```aruco_detect``` который по запросу производит поиск и детекции меток. Возвращается номер самой большой найденной метки. 


Используется тип сообщения ```ArucoDetect```

```
---
uint16 id
uint16 size
```

Где 
`id` Номер найденного маркера
`size` Размер маркера (для оценки расстояния)

Для того, чтобы вывести id найденной метки необходимо прослушать топик ``` /aruco_marker ```:
```
rostopic echo /aruco_marker
```


