<template>
    <div v-loading="data.loading">
        <el-form
            :model="data.form"
            :rules="myRule"
            label-suffix=":"
            label-width="100px"
            :disabled="props.disabled"
        >
            <template v-for="(item,index) in props.data" :key="index" >
                <el-form-item :label="item.label" :prop="item.name">
                    <el-date-picker
                        v-if="item.type === 'picker'"
                        size="default"
                        v-model="data.form[item.name]"
                        type="datetime"
                        :default-value="new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDay())"
                        clearable
                    />
                    <template v-else-if="item.type === 'link'">
                        <svg-icon name="ep:money" style="margin-right: 10px"/>
                        <el-link :href="item.link.src" type="primary" target="_blank">{{item.link.name}}</el-link>
                    </template>
                    <template v-else-if="item.type === 'upload'">
                        <div>//上传还没写</div>
                    </template>
                    <el-input
                        v-else
                        v-model="data.form[item.name]"
                        :placeholder="item.placeholder"
                        clearable
                    />
                </el-form-item>
            </template>
        </el-form>
    </div>
</template>

<script setup>
import {ElMessage} from "element-plus"

const props = defineProps({
    data: {
        type: Array,
        default: []
    },
    rules: {
        type: Object,
        default: {}
    },
    disabled: {
        type: Boolean,
        default: false
    },
    type: {
        type: String,
        default: null
    },
    id: {
        type: [Number, String],
        default: null
    }
})

const data = ref({
    loading: false,
    form: {},
})
const myVisible = ref(false)

const myRule = computed({
    get:function(){
        return props.rules
    }
})

onMounted(() => {
    getForm();
})

//初始化数据
function getForm(){//通过id获取数据
    data.value.form =  {
        'jobName': 'a',
        'CourseName': '网络攻防',
        'jobRemarks': '无',
        'jobStartTime': '1667117394',
        'jobEndTime': new Date().getTime()/1000,
        'detailFile': {
            src: 'https://ctf.show/',
            name: 'ctf'
        }
    }
    // props.data.map(item => {
    //     data.value.form[item.name]= '';
    //     if(item.hasOwnProperty('submitTime')){
    //         data.value.submitTime = new Date(item.submitTime*1000)
    //         delete data.value.form[item.name]
    //     }
    //     if(item.hasOwnProperty('type'))
    //         delete data.value.form[item.name]
    // })
}

defineExpose({
    submit(callback){
        console.log("提交")
        callback && callback()
    }
})
</script>

<style lang="scss" scoped>
.upload-video ::v-deep {
    margin: 0;
    .el-upload-dragger {
        padding: 0;
        border: none;
    }
}
</style>
