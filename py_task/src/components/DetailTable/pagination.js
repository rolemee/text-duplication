export function usePagination() {
    const pagination = ref({
        currentPage: 1,//当前页
        size: 10,
        total: 0,
        sizes: [10, 20, 50, 100],
        layout: 'total, sizes, ->, prev, pager, next, jumper'
    })

    function getParams(params={}) {//获取当前参数
        const baseParams = {
            pageIndex: pagination.value.currentPage,
            pageSize: pagination.value.size
        }
        Object.assign(baseParams, params)
        return baseParams
    }

    function onSizeChange(size) {
        return new Promise(resolve => {
            pagination.value.size = size
            resolve()
        })
    }

    function onCurrentChange(page) {
        return new Promise(resolve => {
            pagination.value.currentPage = page
            resolve()
        })
    }

    return {
        pagination,
        getParams,
        onSizeChange,
        onCurrentChange
    }
}

export default usePagination()
