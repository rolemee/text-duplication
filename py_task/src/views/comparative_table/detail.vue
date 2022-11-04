<script setup name="taskManageList">
import api from '@/api/index'

const route = useRoute()
const router = useRouter()

function goBack() {
    router.push({name: 'studentJobManageList'})
}

const data = ref({
    loading: false,
    // 表格
    tableData: [],
    columns: [
        {
            prop: 'id1',
            label: '文件1'
        },
        {
            prop: 'id2',
            label: '文件2'
        },
        {
            prop: 'similarity',
            label: '重复率'
        }
    ],
    option: {
        stripe: true,
        fit: true,
        border: true,
        pagination: false,
        operation: false
    }
})

function handleClick(val) {
    // console.log(val)
    router.push({
        name: 'detailMatch',
        params: {
            homeworkId: route.params.workId,
            leftName: val.id1,
            rightName: val.id2
        }
    })
}

onMounted(() => {
    data.value.loading = true
    api.get('/testb', {
        params: {
            homeworkId: route.params.workId,
        }
    }).then(res => {
        data.value.tableData = res.data
        data.value.loading = false
    }).catch(() => {
        data.value.loading = false
    })
})

</script>

<template>
    <div>
        <page-header title="学生作业查重表">
            <el-button size="default" round @click="goBack">
                <template #icon>
                    <el-icon>
                        <svg-icon name="ep:arrow-left" />
                    </el-icon>
                </template>
                返回
            </el-button>
        </page-header>
        <page-main v-loading="data.loading">
           <DetailTable
               :tableData="data.tableData"
               :columns="data.columns"
               :option="data.option"
               @handleClick="handleClick"
           />
        </page-main>
    </div>
</template>

<style scoped lang="scss">
//scss
</style>
