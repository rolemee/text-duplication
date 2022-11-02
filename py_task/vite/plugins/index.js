import vue from '@vitejs/plugin-vue'

import createRestart from './restart'
import createJsx from './jsx'
import createHtml from './html'
import createAutoImport from './auto-import'
import createComponents from './components'
import createSetupExtend from './setup-extend'
import createSvgIcon from './svg-icon'
import createMock from './mock'
import createLayouts from './layouts'
import createPages from './pages'
import createCompression from './compression'
import createSpritesmith from './spritesmith'
import createBanner from './banner'

export default function createVitePlugins(viteEnv, isBuild = false) {
    const vitePlugins = [vue()]
    !isBuild && vitePlugins.push(createRestart())
    vitePlugins.push(createJsx())
    vitePlugins.push(createHtml(viteEnv, isBuild))
    vitePlugins.push(createAutoImport())
    vitePlugins.push(createComponents(isBuild))
    vitePlugins.push(createSetupExtend())
    vitePlugins.push(createSvgIcon(isBuild))
    vitePlugins.push(createMock(viteEnv, isBuild))
    vitePlugins.push(createLayouts())
    vitePlugins.push(createPages())
    isBuild && vitePlugins.push(...createCompression(viteEnv))
    vitePlugins.push(...createSpritesmith(isBuild))
    vitePlugins.push(createBanner())
    return vitePlugins
}
