<script setup name="DetailShow">
import api from '@/api/index'

const route = useRoute()
const router = useRouter()

function goBack() {
    router.push({ name: 'taskManageList' })
}

const data = ref({
    loading: false,
    title: {
        right: route.params.rightName,
        left: route.params.leftName
    },
    leftData: '',
    rightData: '',
    left: {
        start: [],
        end: []
    },
    right: {
        start: [],
        end: []
    },
    colors: [],
    colorLists: [
        'rgba(230,25,75,0.8)',
        'rgba(60,180,75,0.84)',
        'rgba(255,225,25,0.8)',
        'rgba(67,99,216,0.81)',
        'rgba(245,130,49,0.82)',
        'rgba(145,30,180,0.79)',
        'rgba(66,212,244,0.8)',
        'rgba(240,50,230,0.83)',
        'rgba(191,239,69,0.81)',
        'rgba(250,190,212,0.8)',
        'blueviolet'
    ]
})

function getData(res, side = 'left') {
    let code = JSON.parse(JSON.stringify(res))
    code = code.replace(eval('/' + '<' + '/g'), '&lt;')
    code = code.replace(eval('/' + '>' + '/g'), '&gt;')
    let cache = code.split('\n')
    cache = cache.filter( s => {
        return s && s.trim()
    })
    // console.log(cache)
    code = JSON.parse(JSON.stringify(cache))
    let beforeStart = []
    let beforeEnd = []
    let flag = false
    let key = 0
    for (let j = 0; j < data.value[side].start.length; j++) {
        if (beforeEnd.indexOf(data.value[side].end[j]) !== -1 || beforeStart.indexOf(data.value[side].start[j]) !== -1) {
            flag = true
            ++key
        } else {
            beforeStart.push(data.value[side].start[j])
            beforeEnd.push(data.value[side].end[j])
            flag = false
        }
        // console.log(j)
        for (let i = data.value[side].start[j] - 1; i < data.value[side].end[j]; i++) {
            let sign
            if (flag) {
                console.log("key"+key)
                sign = `<div style="background-color: ${data.value.colorLists[data.value.colors[j]]};width: 100%;height: 100%;"></div><div></div>`
                code[i] = code[i].replace('<div></div>', `${sign}`)
            }else {
                let cacheData = cache[i]
                cache[i] = `<div style="position: relative;float: left;z-index: 999 ">${cache[i]}</div>`
                sign = `<span style="color: white;overflow: hidden"><div style="left:0" class="sign">${cache[i]}<div class="sign-content" style="display: flex">
<div style="background-color: ${data.value.colorLists[data.value.colors[j]]};width: 100%;height: 100%;"></div><div></div></div></div></span>`
                code[i] = code[i].replace(cacheData, `${sign}`)
            }
            console.log(sign)
            // right[i] = right[i].replace(cache[i], `${sign}`)
            // console.log(cache[i])
            console.log(code[i])
        }
    }
    let dataType = side === 'right' ? 'rightData' : 'leftData'
    for (let i = 0; i < code.length; i++) {
        if (code[i].indexOf('<span') !== -1) {
            data.value[dataType] += code[i]
        }else {
            data.value[dataType] += code[i] + '\n'
        }
    }
}
onMounted(() => {
    data.value.loading = true
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
            tmp++
        })
        // console.log(data.value.right)
        api.get(`testc?filename=${route.params.rightName}`).then(res => {
            getData(res, 'right')
            data.value.loading = false
        }).catch(() => {
            data.value.loading = false
        })
        api.get(`testc?filename=${route.params.leftName}`).then(res => {
            getData(res,'left')
            data.value.loading = false
        }).catch(() => {
            data.value.loading = false
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
        <page-main v-loading="data.loading">
            <el-row :gutter="8">
                <el-col :span="12">
                    <el-collapse
                        class="file file-left"
                        accordion
                    >
                        <el-collapse-item>
                            <template #title>
                                <div class="title">
                                    {{ data.title.left }}
                                </div>
                            </template>
                            <el-scrollbar height="360px">
                                <div class="content-text" v-html="data.leftData" />
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
                                    {{ data.title.right }}
                                </div>
                            </template>
                            <el-scrollbar height="360px">
                                <div class="content-text" v-html="data.rightData" />
                            </el-scrollbar>
                        </el-collapse-item>
                    </el-collapse>
                </el-col>
            </el-row>
<!--            <span style="color: black;width: 400px;height: 25px;background-color: greenyellow">-->
<!--                <div style="position: relative; top:0;background-color: cyan;z-index: 1;width: 100%;height: 25px;overflow: hidden;">-->
<!--                    <div style="z-index:999;float: left;position: relative" class="T">    for(int j=n-1;i&gt;=0;i&#45;&#45;)</div>-->
<!--                    <div style="position: absolute;top: 0; display: flex;width: 100%;height: 100%;">-->
<!--                        <div style="box-shadow: 0 0 5px 20px blueviolet;width: 100%;height: 100%;z-index: 1"/>-->
<!--                        <div style="background-color: violet;width: 100%;height: 100%;z-index: 1"></div>-->
<!--                    </div>-->
<!--                </div>-->
<!--            </span>-->
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
:deep(.sign) {
    width: 100%;
    height: 25px;
    position: relative;
    top: 0;
    overflow: hidden;
    z-index: 1;
    .sign-content {
        width: 100%;
        height: 100%;
        position: absolute;
        top:0;
        //filter: blur(1px);
        //clear:both;
    }
}
</style>
