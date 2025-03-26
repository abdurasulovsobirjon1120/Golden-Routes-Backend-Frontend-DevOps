plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("kotlin-kapt")
}

android {
    namespace = "com.azamovme.golden_routes"
    compileSdk = 35
    kapt {
        correctErrorTypes = true
    }
    defaultConfig {
        applicationId = "com.azamovme.golden_routes"
        minSdk = 24
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = "1.8"
    }
    buildFeatures {
        viewBinding = true
    }
}

dependencies {
    //noinspection GradleDependency
    implementation("androidx.core:core-ktx:1.9.0")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.constraintlayout:constraintlayout:2.2.0")
    implementation("androidx.activity:activity-ktx:1.9.3")
    implementation("androidx.paging:paging-runtime-ktx:3.3.5")
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
    // Koin
    implementation("io.insert-koin:koin-android:3.5.0")
    implementation("androidx.constraintlayout:constraintlayout:2.2.0")
    implementation("androidx.navigation:navigation-runtime-ktx:2.8.4")
    implementation("androidx.navigation:navigation-ui-ktx:2.8.4")
    implementation("androidx.navigation:navigation-fragment-ktx:2.8.4")

    // sdp
    implementation("com.intuit.sdp:sdp-android:1.1.1")
    implementation("com.intuit.ssp:ssp-android:1.1.1")


    // preference
    implementation("androidx.preference:preference-ktx:1.2.1")


    // gson
    implementation("com.google.code.gson:gson:2.10.1")


    //Chucker
    debugImplementation("com.github.chuckerteam.chucker:library:4.0.0")
    releaseImplementation("com.github.chuckerteam.chucker:library-no-op:4.0.0")
//
    /**
     * Glide
     * */
    implementation("com.github.bumptech.glide:glide:4.15.1")
    //noinspection KaptUsageInsteadOfKsp
    kapt("com.github.bumptech.glide:compiler:4.15.1")

    // tapadoo
    implementation("com.github.tapadoo:alerter:7.2.4")


    //Biometric
    implementation("androidx.biometric:biometric:1.1.0")

    // tapadoo
    implementation("com.github.tapadoo:alerter:7.2.4")

    // Animated Theme
    implementation ("io.github.imandolatkia:animatedThemeManager:1.1.2")

    //Theme animation
    implementation("com.airbnb.android:lottie:5.2.0")

}