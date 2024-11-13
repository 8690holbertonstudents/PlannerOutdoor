<template>
  <div class="home-container">
    <div class="home-item">
      <h2>Welcome to PlannerOutdoor !</h2>
      <h3>
        This project enables users with an account to plan their outdoor
        activities, taking into account weather conditions and any allergies
        they may have.
      </h3>
      <h3>
        This project is not yet complete, and unfortunately not all features
        have been implemented.
      </h3>
    </div>
    <div class="home-item">
      <h2>Core technologies</h2>
      <div class="logo-container">
        <a
          href="https://www.djangoproject.com/"
          title="Django framework"
          target="_blank"
          class="logo-item"
        >
          <img src="images/django.png" alt="django" />
        </a>
        <a
          href="https://www.django-rest-framework.org/"
          title="Django rest framework"
          target="_blank"
          class="logo-item"
        >
          <img src="images/django_rest_framework.png" alt="django-drf" />
        </a>
        <a
          href="https://vuejs.org/"
          title="Vue.js framework"
          target="_blank"
          class="logo-item"
        >
          <img src="images/vue_js.png" alt="vue.js" />
        </a>
        <a
          href="https://www.mysql.com/"
          title="Mysql database"
          target="_blank"
          class="logo-item"
        >
          <img src="images/mysql_logo.png" alt="mysql" />
        </a>
        <a
          href="https://openweathermap.org/"
          title="Openweather API"
          target="_blank"
          class="logo-item"
        >
          <img src="images/openweather.png" alt="openweather" />
        </a>
      </div>
    </div>
    <div class="home-item">
      <h2>API documentation & administration</h2>
      <div class="api-container">
        <a
          href="http://localhost:8020/swagger/"
          target="_blank"
          class="api-item"
        >
          <img
            src="/images/screen_capture_api_swagger.png"
            title="Swagger documentation"
            alt="swagger"
          />
        </a>
        <a
          href="http://localhost:8020/redoc/"
          title="Redoc documentation"
          target="_blank"
          class="api-item"
        >
          <img src="/images/screen_capture_api_redoc.png" alt="redoc" />
        </a>
        <a
          href="http://localhost:8020/admin/"
          title="Django admin console"
          target="_blank"
          class="api-item"
        >
          <img src="/images/screen_capture_api_django-admin.png" alt="admin" />
        </a>
      </div>
    </div>
    <div class="home-item">
      <h2>To implement</h2>
      <h3>- Full test process (back & front)</h3>
      <h3>- Fetch an allergens API</h3>
      <h3>- Business logic for planification</h3>
      <h3>- Include weather map</h3>
      <h3>- Email alerts</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: var(--header-footer-height);
  gap: 50px;
  flex-wrap: wrap;
}

.home-item {
  background-color: var(--color-background-item);
  border-radius: var(--default-radius);
  margin-top: 50px;
  padding: 20px;
  flex-basis: 500px;
}

.logo-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.logo-item {
  padding: 10px;
}

.logo-item img {
  min-width: 60px;
  height: 60px;
}

.api-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.api-item {
  padding: 10px;
}

.api-item img {
  min-width: 150px;
  height: 150px;
}

h1,
h2 {
  text-align: center;
  margin-bottom: 50px;
}

h3 {
  text-align: justify;
  margin-bottom: 50px;
}
</style>
