<script setup name="DetailShow">
import api from '@/api/index'

const route = useRoute()
const router = useRouter()

function goBack() {
    router.push({name: 'taskManageList'})
}

const data = ref({
    title: {
        right: 'r',
        left: 'l'
    },
    leftData: '',
    rightData: '',
    left: {
        start: 0,
        end: 0
    },
    right: {
        start: 0,
        end: 0
    }
})
const setKeyWord  = ref()

onMounted(() => {
    api.get('/testd', {
        params: {
            homeworkId: route.params.homeworkId,
            file1: route.params.rightName,
            file2: route.params.leftName
        }
    }).then(res => {
        data.value.left.start = res.data[0].start1
        data.value.right.start = res.data[0].start2
        data.value.left.end = res.data[0].end1
        data.value.right.end = res.data[0].end2
        // console.log(data.value.right)
        api.get(`testc?filename=${route.params.leftName}`).then(res => {
            let left = JSON.parse(JSON.stringify(res))
            left = left.replace(eval("/"+'<'+"/g"), '&lt;')
            let cache = left.split('\n')
            for (let i = data.value.left.start-1; i < data.value.left.end; i++ ) {
                left = left.replace(cache[i], `<span style="color:red">${cache[i]}</span>`);
            }
            data.value.leftData = left
            // console.log(cache)
        })
        api.get(`testc?filename=${route.params.rightName}`).then(res => {
            let right = JSON.parse(JSON.stringify(res))
            right = right.replace(eval("/"+'<'+"/g"), '&lt;')
            let cache = right.split('\n')
            for (let i = data.value.right.start-1; i < data.value.right.end; i++ ) {
                right = right.replace(cache[i], `<span style="color:red">${cache[i]}</span>`);
            }
            data.value.rightData = right
            // console.log(cache)
        })
    })

})

</script>

<template>
    <div>
        <page-header title="学生作业详情">
            <el-button size="default" round @click="goBack">
                <template #icon>
                    <el-icon>
                        <svg-icon name="ep:arrow-left" />
                    </el-icon>
                </template>
                返回
            </el-button>
        </page-header>
        <page-main >
            <el-row :gutter="8">
                <el-col :span="12">
                    <el-collapse
                        class="file file-left"
                        accordion
                    >
                        <el-collapse-item>
                            <template #title>
                                <div class="title">
                                    {{data.title.left}}
                                </div>
                            </template>
                            <el-scrollbar height="360px">
                                <div class="content-text" v-html="data.leftData"/>
                            </el-scrollbar>
                        </el-collapse-item>
                    </el-collapse>
                </el-col>
                <el-col :span="12">
                    <el-collapse
                        class="file file-right"
                    >
                        <el-collapse-item>
                            <template #title>
                                <div class="title">
                                    {{data.title.right}}
                                </div>
                            </template>
                            <el-scrollbar height="360px">
                                <div class="content-text" v-html="data.rightData">
                                </div>
                            </el-scrollbar>

                        </el-collapse-item>
                    </el-collapse>
                </el-col>
            </el-row>
        </page-main>
    </div>
</template>

<style scoped lang="scss">
//scss
:deep(.file-right .el-collapse-item__header){
    background-color: rgba(209, 237, 196, 0.89);
}
:deep(.file-left .el-collapse-item__header){
    background-color: rgba(160, 207, 255, 0.82);
}
:deep(.file .el-collapse-item__header) {
    text-align: justify;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: 18px;
    font-weight: 550;
    line-height:1.7;
    border-radius: 8px;
    overflow: hidden;
    transition: all 0.5s ease;
}
:deep(.file  .is-active) {
    border-radius: 8px 8px 0 0;
}
:deep(.file .el-collapse-item) {
    box-shadow: 1px 1px 2px rgba(109, 109, 109, 0.69);
    border-radius: 8px;
    .content-text {
        white-space: pre-wrap;
        word-break: break-all;
        word-wrap: break-word;
    }
}
:deep(.title) {
    margin-left: 15px;
}

</style>
