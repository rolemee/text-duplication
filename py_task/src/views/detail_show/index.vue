<script setup name="DetailShow">
import api from '@/api/index'
import 'monaco-editor/esm/vs/basic-languages/monaco.contribution'
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api.js'
const route = useRoute()
const router = useRouter()
const activeNamesList = ref([])
const activeNames = ref(['1'])
function goBack() {
    router.push({ name: 'taskManageList' })
}

const data = ref({
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
    },
    colors: [],
    issame: 0,
    colorlists: [
        '#e6194B',
        '#3cb44b',
        '#ffe119',
        '#4363d8',
        '#f58231',
        '#911eb4',
        '#42d4f4',
        '#f032e6',
        '#bfef45',
        '#fabed4',
        'blueviolet'
    ]
})

onMounted(() => {
    api.get('/testd', {
        params: {
            homeworkId: route.params.homeworkId,
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
            data.value.colors.push(tmp)
            activeNamesList.value.push(tmp)
            tmp++
        })
        // console.log(data.value.right)
        api.get(`testc?filename=${route.params.rightName}`).then(res => {
            let right = JSON.parse(JSON.stringify(res))
            // right = right.replace(eval('/' + '<' + '/g'), '&lt;')
            // right = right.replace(eval('/' + '<' + '/g'), '&gt;')
            let cache = right.split('\n')
            right = cache
            data.value.rightDataList.push(cache)
            for (let j = 0; j < data.value.right.start.length; j++) {
                // console.log(data.value.right.start[j])
                for (let i = data.value.right.start[j] - 1; i < data.value.right.end[j]; i++) {
                    if (right[i].indexOf('style="color') !== -1) {
                        continue
                    }
                    // right[i] = right[i].replace(cache[i], `<span style="color: ${data.value.colorlists[data.value.colors[j]]}">${cache[i]}</span>`)
                }
            }
            for (let i = 0; i < right.length; i++) {
                data.value.rightData += right[i] + '\n'
            }
            let setKeyWord  = ref()
            let monacoInstance = monaco.editor.create(document.getElementById('right-monaco'), {
                value: data.value.rightData,
                language: 'c',
                fontSize: 15,
                readOnly: true
            })

            // console.log(cache)
        })
        api.get(`testc?filename=${route.params.leftName}`).then(res => {
            let left = JSON.parse(JSON.stringify(res))
            // left = left.replace(eval('/' + '<' + '/g'), '&lt;')
            // left = left.replace(eval('/' + '>' + '/g'), '&gt;')

            let cache = left.split('\n')
            left = left.split('\n')
            data.value.leftDataList.push(left)
            console.log(data.value.left.start)
            console.log(data.value.left.end)
            console.log(left)
            console.log(cache)
            let before_start = '0'
            let before_end = '0'
            let flag = -1
            for (let j = 0; j < data.value.left.start.length; j++) {
                if (before_end === data.value.right.end[j] && before_start === data.value.right.start[j]) {
                    console.log(1)
                } else {
                    before_start = data.value.right.start[j]
                    before_end = data.value.right.end[j]
                    flag++
                }
                for (let i = data.value.left.start[j] - 1; i < data.value.left.end[j]; i++) {
                    // left[i] = left[i].replace(cache[i], `<span style="color: ${data.value.colorlists[data.value.colors[flag]]}">${cache[i]}</span>`)
                }
            }
            for (let i = 0; i < left.length; i++) {
                data.value.leftData += left[i] + '\n'
            }
            let setKeyWord  = ref()
            let monacoInstance = monaco.editor.create(document.getElementById('left-monaco'), {
                value: data.value.leftData,
                language: 'c',
                fontSize: 15,
                readOnly: true
            })

            // console.log(cache)
        })
        setTimeout(() => {

            for (let i = 0; i < data.value.left.start.length; i++) {
                let leftDataDiff = ''
                let rightDataDiff = ''
                for (let j = data.value.left.start[i] - 1; j < data.value.left.end[i]; j++) {
                    // eslint-disable-next-line no-unused-vars
                    leftDataDiff += j + 1 + ': ' + data.value.leftDataList[0][j] + '\n'
                }
                for (let j = data.value.right.start[i] - 1; j < data.value.right.end[i]; j++){
                    rightDataDiff += j + 1 + ': ' + data.value.rightDataList[0][j] + '\n'
                }
                console.log(rightDataDiff)
                console.log(leftDataDiff)
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

                let leftMonaco = monaco.editor.create(document.getElementById('left-monaco-list-' + i), {
                    value: leftDataDiff,
                    language: 'c',
                    readOnly: true,
                    fontSize: 15,
                    theme:'myTheme'
                })
                let rightMonaco = monaco.editor.create(document.getElementById('right-monaco-list-' + i), {
                    value: rightDataDiff,
                    language: 'c',
                    readOnly: true,
                    fontSize: 15,
                    theme: 'myTheme'
                })

                // let originalModel = monaco.editor.createModel(
                //     leftDataDiff,
                //     'cpp'
                // )
                // let modifiedModel = monaco.editor.createModel(
                //     rightDataDiff,
                //     'cpp'
                // )
                // console.log('left-monaco-list-' + i)
                // console.log(document.getElementById('left-monaco-list-' + i))
                // let diffEditor = monaco.editor.createDiffEditor(document.getElementById('left-monaco-list-' + i), {
                //     // You can optionally disable the resizing
                //     enableSplitViewResizing: false
                // })
                // diffEditor.setModel({
                //     original: originalModel,
                //     modified: modifiedModel
                // })
            }
        }, 1000)

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
        <page-main v-for="(item, index) in data.left.start.length">
            <el-row :gutter="8">
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
