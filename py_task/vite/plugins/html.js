import { createHtmlPlugin } from 'vite-plugin-html'


export default function createHtml(env, isBuild) {
    const { VITE_APP_TITLE } = env
    const html = createHtmlPlugin({
        inject: {
            data: {
                title: VITE_APP_TITLE,
                copyrightScript: ''
            }
        },
        minify: isBuild
    })
    return html
}
