<template>
  <main class="weather-view">
    <div v-if="loading">
      <h2>title</h2>
    </div>
    <div v-else>
      <h3>error</h3>
    </div>
  </main>
</template>

<template>
  <main class="weather-view">
    <div v-if="!loading">
      <div v-if="city.name && forecast.list && forecast.list.length">
        <h2 class="title">Weather at {{ city.name }}</h2>
        <div class="weather-container">
          <div
            v-for="(item, index) in forecast.list"
            :key="index"
            class="weather-item"
          >
            <p class="month-year">{{ formatMonthYear(item.dt) }}</p>
            <p class="day">{{ formatDay(item.dt) }}</p>
            <p class="temperature">
              {{ convertTemp(item.temp.day) }}°C /
              {{ convertToFahrenheit(item.temp.day) }}°F
            </p>
            <img
              v-if="item.weather[0].icon"
              :src="`http://openweathermap.org/img/wn/${item.weather[0].icon}@2x.png`"
              :alt="item.weather[0].description"
            />
          </div>
        </div>
      </div>
      <div v-else>
        <h3 class="title">No weather data or bad city name</h3>
      </div>
    </div>
  </main>
</template>
