<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import todoService from '@/services/ToDoService'

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'TEST',
    };
  },
  methods: {
    getMessage() {
      todoService.getPong()
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>