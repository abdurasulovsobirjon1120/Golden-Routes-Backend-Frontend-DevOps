package com.azamovme.golden_routes.themes

import android.content.Context
import android.graphics.drawable.Drawable
import android.view.View
import androidx.core.content.ContextCompat
import com.azamovme.golden_routes.R
import com.azamovme.golden_routes.utils.MyAppTheme

class LightTheme : MyAppTheme {

    companion object {
        const val ThemeId = 0
    }

    override fun id(): Int {
        return ThemeId
    }

    override fun fragmentBackgroundColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.main_background)
    }

    override fun activityBottomNavViewBackColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.card_background)
    }

    override fun statusBarColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.main_background)
    }

    override fun getStatusBarType(context: Context): Int {
        return     View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR

    }

    override fun fragmentLargeTextColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.textColor)
    }

    override fun fragmentSmallTextColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.textColor)
    }

    override fun fragmentSearchCardColor(context: Context): Int {
        return ContextCompat.getColor(context, R.color.light_gray)
    }

    override fun fragmentCheckboxDrawable(context: Context): Drawable {
        return ContextCompat.getDrawable(context, R.drawable.background_indicator_enabled)!!
    }

    override fun fragmentBackDrawable(context: Context): Drawable {
        return ContextCompat.getDrawable(context, R.drawable.ic_round_arrow_back_ios_new_24)!!
    }

}