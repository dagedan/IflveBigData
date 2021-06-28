const propsExtend = (propsObj) => {
    let sb = Object.entries(propsObj).reduce((a,b) => {
        return a += `${b[0]}="${b[1]}" `
    }, '')
    console.log(sb)
}

const MInput = {
    props: ['config'],
    data() {
        return {
            propsExtendStr: ''
        }
    },
    mounted() {
        this.propsExtendStr = propsExtend(this.config.prototype)
    },
    template: `<div>
                    <label :for="config.name" v-text="config.label"></label>
                    <input ${propsExtend(this.config.prototype)}>
                </div>`
}