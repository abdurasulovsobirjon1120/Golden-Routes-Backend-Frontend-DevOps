package com.azamovme.golden_routes.utils

import android.app.ActionBar
import android.app.Activity
import android.app.Dialog
import android.content.Context
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.view.Gravity
import com.azamovme.golden_routes.R
import com.tapadoo.alerter.Alerter

object DialogUtils {

    fun createChangeDialog(
        activity: Activity,
        title: String? = null,
        message: String? = null,
        color: Int
    ) {

        if (title != null) {
            Alerter.create(activity = activity)
                .setTitle(title = title)
                .setText(message.toString())
                .setBackgroundColorRes(colorResId = color)
                .show()
        }
    }

    fun createTapadooDialog(
        activity: Activity,
        title: String? = null,
        message: String? = null,
        color: Int
    ) {

        if (title != null) {
            Alerter.create(activity = activity)
                .setTitle(title = title)
                .setText(message.toString())
                .setBackgroundColorRes(colorResId = color)
                .show()
        }
    }

    fun loadingDialog(context: Context): Dialog{
        val dialog = Dialog(context)
        dialog.setContentView(R.layout.loading_dialog)
        dialog.window?.setLayout(ActionBar.LayoutParams.WRAP_CONTENT, ActionBar.LayoutParams.WRAP_CONTENT)
        dialog.window?.setGravity(Gravity.CENTER)
        dialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
        dialog.setCancelable(false)

        return dialog
    }
}