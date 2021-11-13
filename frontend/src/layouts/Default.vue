<template>
  <div class="container">
    <nav>
      <ul>
        <li><strong>Star Wars Explorer</strong></li>
      </ul>
      <ul>
        <li><a href="#">Collections</a></li>
      </ul>
    </nav>
    <slot />

    <ClientOnly>
      <notifications
        :position="nConfig.position"
        :duration="nConfig.duration"
      />
    </ClientOnly>
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