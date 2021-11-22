<template>
  <div class="home">
    <MainContent/>
  </div>
</template>

<script>
// @ is an alias to /src
import MainContent from '@/components/Content/MainContent.vue'

export default {
  name: 'Home',
  components: {
    MainContent
  }
}
</script>
