<template>
    <div>
        <el-form
            :inline="true"
            :model="data.search"
            :rules="props.search.rules"
            label-suffix=":"
            class="searchBack"
        >
            <el-form-item v-if="props.search.datePick" label="查询日期">
                <el-date-picker
                    size="default"
                    v-model="data.time"
                    type="datetimerange"
                    range-separator="至"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期"
                    :default-value="defaultTime"
                    clearable
                />
            </el-form-item>
            <template v-for="(item,index) in props.search.detailForm" :key="index">
                <el-form-item :label="item.label" :prop="item.name">
                    <el-select
                        v-if="item.type === 'select'"
                        v-model="data.search[item.name]"
                        clearable
                        filterable
                        remote
                        :remote-method="remoteMethod"
                        @change="onChange"
                        @focus="data.selectType = item.name"
                        remote-show-suffix
                        :loading="data.loading"
                        :placeholder='"请输入"+item.label'
                        :loading-text="item.loadingText || 'loading'"
                    >
                        <el-option
                            v-for="(option,index) in props.options[item.name]"
                            :key="index"
                            :label="option.label"
                            :value="option.value"
                        />
                    </el-select>
                    <el-input
                        v-else
                        v-model="data.search[item.name]"
                        :placeholder='"请输入"+item.label'
                        clearable
                    />
                </el-form-item>
            </template>
            <el-form-item>
                <el-button
                    :loading="loading"
                    type="primary"
                    style="font-size: 13px;text-align: center;font-weight: 400;"
                    size="small"
                    @click="getDataList"
                >
                    <svg-icon name="ep:search" style="margin-right: 5px"/>
                    搜索
                </el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup name="TopSearch">
import {onMounted, computed, onBeforeUpdate} from 'vue'

const { proxy } = getCurrentInstance();

const props = defineProps({
    search: {
        type: Object,
        default: {
            detailForm:[],
            rules: null,
            datePick: false,
        }
    },
    options: {
        type: Object,
        default: {}
    }
})

const $myEmit = defineEmits(['handleSearch','remoteMethod','onChange'])

const data = ref({
    search: { },
    time: [new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDate()-14),
        new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDate()+1)],
    loading: false,
    selectType: null
})

const defaultTime = ref([
    new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDate()-14),
    new Date(new Date().getFullYear(),new Date().getMonth(),new Date().getDate()+1)
])

let loading = ref(false)

onMounted(() => {
    getForm();
})
// onBeforeUpdate(() => {
//     getForm();
// })

//初始化搜索表单
function getForm() {
    if(props.search.detailForm.length !== 0 ){
        props.search.detailForm.map(item => {
            data.value.search[item.name]= '';
        })
    }
}
//下拉框
function onChange(val) {
    $myEmit('onChange', {
        type: data.value.selectType,
        value: val
    })
}
function remoteMethod(query) {
    data.value.loading = true
    $myEmit('remoteMethod', {
        query: query,
        type: data.value.selectType
    },() => {
        data.value.loading = false
    })
}
//搜索
function getDataList() {
    loading.value = true
    // console.log(JSON.stringify(data.value.time))
    if (data.value.time) {
        // console.log("/")
        data.value.search['startTime'] = data.value.time[0]
        data.value.search['endTime'] = data.value.time[1]
    }
    // console.log(JSON.stringify(data.value.search))
    $myEmit('handleSearch',data.value.search,() =>{
        loading.value = false
        // data.value.search = {}
        // data.value.time = ''
        // getForm()
    });
}
</script>

<style lang="scss" scoped>
.searchBack{
    margin: 0 0 10px 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    .el-form-item{
        position: relative;
        top:7px;
        //margin-left: 10px;
        font-size: 14px;
        font-weight: 700;
        color: #606266;
        .el-input{
            font-size: inherit;
        }
    }
}
</style>
