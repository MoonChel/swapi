<template>
  <div class="container">
    <nav>
      <ul>
        <li>
          <strong><router-link to="/">Star Wars Explorer</router-link></strong>
        </li>
      </ul>
      <ul>
        <li>
          <router-link to="/">Collections</router-link>
        </li>
      </ul>
    </nav>

    <router-view />

    <notifications :position="nConfig.position" :duration="nConfig.duration" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      nConfig: {
        position: "bottom right",
        duration: 1000,
      },
    };
  },
};
</script>