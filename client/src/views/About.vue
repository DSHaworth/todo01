<template>
  <div>
    <p>{{ msg }}</p>

    <input placeholder="To Do Item" v-model="toDoItem" ><button type="Button" v-on:click="save()">Save</button>
    <p>To Do Item is: {{ toDoItem }}</p>

    <ul class="normal">
      <li class="" v-for = "(item) in toDoItems" :key="item">{{item}}</li>
    </ul>        

  </div>
</template>

<style scoped>
  .normal{
    text-align: left;
  }
</style>

<script>
import todoService from '@/services/ToDoService'

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'TEST',
      toDoItem: '',
      toDoItems: []
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
    getToDoList(){
      todoService.getToDoList()
        .then((res) => {
          this.toDoItems = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    save(){
      todoService.saveItem({"item": this.toDoItem})
        .then((res) => {
          this.toDoItems = res.data;
          this.toDoItem = "";
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
    this.getToDoList();
  },
};
</script>