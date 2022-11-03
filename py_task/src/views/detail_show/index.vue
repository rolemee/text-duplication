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
    rightData: ''
})
const setKeyWord  = ref()

onMounted(() => {
    let  str = '#include<bits/stdc++.h>\n' +
        'using namespace std;\n' +
        'int main(){\n' +
        '\tint n;\n' +
        '\twhile(cin>>n){\n' +
        '\t\tint a[1000]={},sum=0,max0=-1;\n' +
        '\t\tfor(int i=0;i>n;i--){\n' +
        '\t\t\tcin>>a[i];\n' +
        '\t\t\tsum+=a[i];\n' +
        '\t\t\tmax0=max(max0,a[i]);\n' +
        '\t\t}\n' +
        '\t\tsort(a,a+n);\n' +
        '\t\tcout<<sum<<" "<<max0<<" ";\n' +
        '\t\tfor(int i=n-1;i>=0;i--)\n' +
        '\t\t\tcout<<a[i]<<" ";\n' +
        '        for(int j=n-1;i>=0;i--)\n' +
        '\t\t\tcout<<a[j]<<" ";\n' +
        '\t\t\t        for(int j=n-1;i>=0;i--)\n' +
        '\t\t\tcout<<a[j]<<" ";\n' +
        '\t\t\t        for(int j=n-1;i>=0;i--)\n' +
        '\t\t\tcout<<a[j]<<" ";\n' +
        '\t\t\t        for(int j=n-1;i>=0;i--)\n' +
        '\t\t\tcout<<a[j]<<" ";\n' +
        '\t\tcout<<endl;\n' +
        '\t}\n' +
        '\treturn 0;\n' +
        '}'
    let cache = str.split('\n')
    console.log(cache)
    let t = []
    for(let i =3 ; i<5; i++) {
        str = str.replace(cache[i]+'\n', '')
        cache[i] = `<span style="color:red">${cache[i]}</span>`
        t.push(cache[i])
        // console.log(cache[i])
        // // console.log(str.replace("/"+cache[i]+"/g", `<span style="color:red">${cache[i]}</span>`))

        // console.log(JSON.stringify(str))
    }
    // cache.join('\n')
    // console.log(cache.join('\n'))
    // console.log(str)
    setKeyWord.value = t.join('\n')
    data.value.leftData = str
    // console.log(data.value.leftData)
    // api.get('/testc?filename=1.cpp').then(res => {
    //     data.value.leftData = res
    //     let cache = JSON.stringify(res).split(/[\n]/)
    //     console.log(cache)
    // })
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
                                <div class="content-text" v-html="setKeyWord">
                                </div>
                                <div class="content-text">
                                    {{data.leftData}}
                                </div>
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
                                <div class="content-text">
                                    {{data.leftData}}
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
