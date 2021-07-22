const ball = {
    props: ['num', 'color'],
    data () {
        return {
            ballNum: null,
            ballColor:null
        }
    },
    mounted (){
        this.ballNum = this.num < 10 ? '0'+this.num : this.num
        this.ballColor = !!this.color
    },
    template: `
        <div class="ball" :class="{blue:ballColor}">{{ballNum}}</div>`
}