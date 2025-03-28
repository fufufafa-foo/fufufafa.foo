<template>
  <div class="banner">
    <img class="avatar" src="/fufufafa-avatar.jpg" alt="fufufafa avatar" />
    <div class="text">
      <span class="subtitle">Your favorite</span>
      <h1 class="title">fufufafa's Quotes</h1>
    </div>
  </div>
</template>

<style scoped>
.banner {
  display: flex;
  justify-content: center;
}

.avatar {
  border-radius: 50%;
  height: 100px;
  width: 100px;
  margin-right: 1rem;
}

.text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 1rem;
}

.title {
  font-size: 1.5rem;
  line-height: unset;
  margin: unset;
}

.subtitle {
  margin-right: 1rem;
}
</style>
