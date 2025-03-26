package com.azamovme.golden_routes.di

import android.os.Build
import androidx.annotation.RequiresApi
import org.koin.android.ext.koin.androidContext
import org.koin.androidx.viewmodel.dsl.viewModel
import org.koin.core.context.loadKoinModules
import org.koin.core.module.Module
import org.koin.dsl.module

//fun injectLoginFeature() = loginFeature
//private val loginFeature by lazy {
//
//    loadKoinModules(
//        listOf(
//            viewModelModule,
//            useCaseModule,
//            repositoryModule,
//        )
//    )
//}

//
//val viewModelModule: Module = module {
//    viewModel { RegisterViewModel(useCase = get(), userDataPreferenceManager = get()) }
//    viewModel { PersonalDataViewModel(useCase = get()) }
//    viewModel { CarDataFillViewModel(useCase = get()) }
//}
//
//val useCaseModule: Module = module {
//    factory { UserDataPreferenceManager(androidContext()) }
//    factory { RegisterUseCase(repository = get()) }
//}
//
//val repositoryModule: Module = module {
//    single<RegisterRepository> {
//        RegisterRepositoryImpl(apiService = get())
//    }
//
//}

