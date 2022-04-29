Для создания контейнера

docker build -t dcimtest . 

#######################

Для загрузки контейнера

docker load dcimtest > dcimtest.tar

#######################

Для запуска контейнера

docker run -p 5000:5000 dcimtest