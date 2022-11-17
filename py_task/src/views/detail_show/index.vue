<script setup name="DetailShow">
import api from '@/api/index'
import 'monaco-editor/esm/vs/basic-languages/monaco.contribution'
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api.js'
const route = useRoute()
const router = useRouter()
const activeNamesList = ref([])
const activeNames = ref(['1'])
function  type_transform(name) {
    if (name === 'py' || name === 'python3') {
        name = 'python'
    } else if (name === 'c++' || name === 'c') {
        name = 'cpp'
    }
    return name
}
function goBack() {
    if (typeof route.params.type === 'undefined') {
        router.push({ name: 'taskManageList' })
    } else if (route.params.type === 'onlyDuplicate') {
        router.push({ name: 'duplicateCheckingList' })
    }
}

const data = ref({
    loading: false,
    title: {
        right: route.params.rightName,
        left: route.params.leftName
    },
    leftData: '',
    rightData: '',
    leftDataList: [],
    rightDataList: [],
    left: {
        start: [],
        end: []
    },
    right: {
        start: [],
        end: []
    }
})

onMounted(() => {
    // console.log(route.params.type)
    // console.log(typeof route.params.type)
    data.value.loading = true
    api.get('/fileDiff', {
        params: {
            homeworkId: route.params.homeworkId,
            filetype: route.params.homeworkType,
            file1: route.params.leftName,
            file2: route.params.rightName
        }
    }).then(res => {
        let tmp = 0
        res.data.forEach(item => {
            // console.log(item.start1)
            data.value.left.start.push(item.start1)
            data.value.right.start.push(item.start2)
            data.value.left.end.push(item.end1)
            data.value.right.end.push(item.end2)
            activeNamesList.value.push(tmp)
            tmp++
        })
        let p = new Promise(resolve => {
            api.post('/getHomeworkContent',{
                homeworkId: route.params.homeworkId,
                filename:  route.params.rightName
            }).then(res => {
                data.value.rightData = res.data.content
                data.value.rightDataList = JSON.parse(JSON.stringify(res.data.content)).split('\n')
                // console.log(data.value.rightDataList)
                console.log(route.params.homeworkType)
                monaco.editor.create(document.getElementById('right-monaco'), {
                    value: data.value.rightData,
                    language: type_transform(route.params.homeworkType),
                    fontSize: 15,
                    readOnly: true
                })
                api.post('/getHomeworkContent',{
                    homeworkId: route.params.homeworkId,
                    filename:  route.params.leftName
                }).then(re => {
                    data.value.leftData = re.data.content
                    data.value.leftDataList = JSON.parse(JSON.stringify(re.data.content)).split('\n')
                    monaco.editor.create(document.getElementById('left-monaco'), {
                        value: data.value.leftData,
                        language: type_transform(route.params.homeworkType),
                        fontSize: 15,
                        readOnly: true
                    })
                    resolve()
                })
            }).catch(() => resolve())
        })
        p.then(() => {
            for (let i = 0; i < data.value.left.start.length; i++) {
                let leftDataDiff = ''
                let rightDataDiff = ''
                for (let j = data.value.left.start[i] - 1; j < data.value.left.end[i]; j++) {
                    // eslint-disable-next-line no-unused-vars
                    leftDataDiff += j + 1 + ': ' + data.value.leftDataList[j] +'\n'
                }
                for (let j = data.value.right.start[i] - 1; j < data.value.right.end[i]; j++){
                    rightDataDiff += j + 1 + ': ' + data.value.rightDataList[j] + '\n'
                }
                monaco.editor.defineTheme('myTheme', {
                    base: 'vs',
                    inherit: true,
                    rules: [{ background: 'EDF9FA' }],
                    colors: {
                        'editor.foreground': '#000000',
                        'editor.background': '#ffffff',
                        'editorCursor.foreground': '#8B0000',
                        'editor.lineHighlightBackground': '#0000FF20',
                        'editorLineNumber.foreground': '#008800',
                        'editor.selectionBackground': '#88000030',
                        'editor.inactiveSelectionBackground': '#88000015'
                    }
                });
                // eslint-disable-next-line no-inner-declarations
                monaco.editor.create(document.getElementById('left-monaco-list-' + i), {
                    value: leftDataDiff,
                    language: type_transform(route.params.homeworkType),
                    readOnly: true,
                    fontSize: 15,
                    theme:'myTheme'
                })
                monaco.editor.create(document.getElementById('right-monaco-list-' + i), {
                    value: rightDataDiff,
                    language: type_transform(route.params.homeworkType),
                    readOnly: true,
                    fontSize: 15,
                    theme: 'myTheme'
                })
            }
            data.value.loading = false
        })
    })
})

</script>

<template>
    <div>
        <page-header :title="route.params.type === 'onlyDuplicate' ? '查重对比详情' : '学生作业详情'">
            <el-button size="default" round @click="goBack">
                <template #icon>
                    <el-icon>
                        <svg-icon name="ep:arrow-left" />
                    </el-icon>
                </template>
                返回
            </el-button>
        </page-header>
        <div v-loading="data.loading">
            <page-main>
                <el-row :gutter="8">
                    <el-col :span="12">
                        <el-collapse
                            v-model="activeNames "
                            class="file file-left"
                            accordion
                        >
                            <el-collapse-item name="1">
                                <template #title>
                                    <div class="title">
                                        {{ data.title.left }}
                                    </div>
                                </template>
                                <div id="left-monaco" style="height: 360px" />
                            </el-collapse-item>
                        </el-collapse>
                    </el-col>
                    <el-col :span="12">
                        <el-collapse
                            v-model="activeNames"
                            class="file file-right"
                        >
                            <el-collapse-item name="1">
                                <template #title>
                                    <div class="title">
                                        {{ data.title.right }}
                                    </div>
                                </template>
                                <div id="right-monaco" style="height: 360px" />
                            </el-collapse-item>
                        </el-collapse>
                    </el-col>
                </el-row>
            </page-main>
            <page-main>
                <div class="subTitle">重复详情</div>
                <el-row :gutter="8">
                    <template v-for="(item, index) in data.left.start.length">
                        <el-col :span="12">
                            <el-collapse
                                v-model="activeNamesList"
                                class="file file-left"
                                accordion
                            >
                                <el-collapse-item :name="index">
                                    <template #title>
                                        <div class="title">
                                            {{ data.title.left }} ：第 {{ data.left.start[index] }} - {{ data.left.end[index] }} 行
                                        </div>
                                    </template>
                                    <div :id="'left-monaco-list-' + index" style="height: 360px" />
                                </el-collapse-item>
                            </el-collapse>
                        </el-col>
                        <el-col :span="12">
                            <el-collapse
                                v-model="activeNamesList"
                                class="file file-right"
                            >
                                <el-collapse-item :name="index">
                                    <template #title>
                                        <div class="title">
                                            {{ data.title.right }} ：第 {{ data.right.start[index] }} - {{ data.right.end[index] }} 行
                                        </div>
                                    </template>
                                    <div :id="'right-monaco-list-' + index" style="height: 360px" />
                                </el-collapse-item>
                            </el-collapse>
                        </el-col>
                    </template>
                </el-row>
            </page-main>
        </div>
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
}
:deep(.title) {
    margin-left: 15px;
}
:deep(.subTitle) {
    text-align: center;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: 20px;
    font-weight: 550;
    margin-bottom: 25px;
    box-shadow: 1px 1px 2px rgba(109, 109, 109, 0.69);
}

</style>
