const TodoItem = {
    props: ['todo'],
    data() {
        return {
            text: '束带结发开始的'
        }
    },
    mounted() {
        console.log(this.text)
    },
    template: `<li v-text="todo.text"></li>`
}