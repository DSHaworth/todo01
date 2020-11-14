<template>
  <div class="left">

    <h1>To Do List</h1>

    <div>    
      <input placeholder="Title" v-model="toDoItem.title" >
    </div>
    <div>
      <input placeholder="Description" v-model="toDoItem.description" >
    </div>
    <div>
      <input type="checkbox"
             v-model="toDoItem.done"> Done
    </div>
    <div>
      <button type="Button" v-on:click="save()">Save</button>
    </div>

    <ul>
      <li class="" v-for = "(item) in toDoItems" :key="item.id" v-on:click="getTask(item.id)"><strong>{{item.title}}</strong>: {{item.description}}</li>
    </ul>    

  </div>
</template>

<style scoped>
  .left{
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
      toDoItem: {
        title: "",
        description: "",
        done: false
      },
      toDoItems: []
    };
  },
  methods: {
    getTasks(){
      todoService.getTasks()
        .then((res) => {
          if(res.data.isValid){
            this.toDoItems = res.data.payload;  
          } else {
            alert(res.data.errorMessage);
          }          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getTask(id){
      todoService.getTask(id)
        .then((res) => {
          if(res.data.isValid){
            this.toDoItem = res.data.payload;
          }
          else {
            alert(res.data.errorMessage);
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    save(){
      todoService.saveItem(this.toDoItem)
        .then((res) => {
          if(res.data.isValid){
            this.toDoItems.push(res.data.payload);
            this.toDoItem.title = "";
            this.toDoItem.description = "";
            this.toDoItem.done = false;
          } else {
            alert(res.data.errorMessage);
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getTasks();
  },
};
</script>